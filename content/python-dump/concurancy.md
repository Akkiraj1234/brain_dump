# Python Concurrency

> **Author** : Akhand Raj  
> **GitHub** : [@Akkiraj1234](https://github.com/Akkiraj1234)  
> **Date**   : 11 July 2025  
> **Status** : Completed

## Topics
- [What is Concurrency?](#what-is-concurrency)
- [GIL (global interpreter lock)](#gil-global-interpreter-lock)
- [Why do we need Concurrency?](#why-do-we-need-concurrency)
- [Asyncio vs Threading vs Multiprocessing](#asyncio-vs-threading-vs-multiprocessing)
---

## What is Concurrency?
Concurrency means doing multiple things at once — logically, not always physically.\
It’s when a program starts a task, pauses it, switches to another task, and keeps rotating. It gives the illusion of parallel work, even on a single CPU core.

### Real-Life Analogy
**Parallelism**: You and your friend cook at the same time — you make Maggi, they wash dishes. Both done at once.

**Concurrency**: You cook Maggi, then while water is boiling, you wash dishes. One CPU doing both tasks — just switching between them smartly.

### Concurrency vs Parallelism
| Concurrency                     | Parallelism                          |
| ------------------------------- | ------------------------------------ |
| Tasks run *logically* at once   | Tasks run *physically* at once       |
| Can happen on **1 core**        | Requires **multiple CPU cores**      |
| Good for I/O & task management  | Good for CPU-intensive computation   |
| Uses threads, coroutines, async | Uses multiprocessing or true threads |

### Tools (Libs) for Concurrency in Python
Python gives you multiple ways to write concurrent programs — but each tool exists for a specific reason, based on what kind of task you're doing.

#### `Threading`
- Creates real OS-level threads (via threading.Thread)
- But because of the GIL, only one thread runs Python code at a time
- Still useful for I/O-bound tasks (like file I/O, user input, waiting on network)
- Not good for CPU-heavy tasks like math loops or image processing

#### `asyncio`
- Uses coroutines, not threads, It’s like saying: "Pause this function, go run something else, come back later"
- Extremely lightweight and scalable — you can run thousands of tasks in Concurrency
- Perfect for I/O-bound stuff like: HTTP requests, Socket communication.
- You use it when your program needs to wait a lot and you want to avoid the cost of threads not good at all for cpu heavy task.

### `multiprocessing`
- Spawns **separate Python processes**
- Each has its own memory space → **no GIL limit**
- good for cpu heavy task. ml tasks.

#### `concurrent.futures.ThreadPoolExecutor`
- Built on top of threading, but makes it easier to use, still block by gil
- Submit tasks, wait for result — that’s it

#### `concurrent.futures.ProcessPoolExecutor`
- Runs tasks using the multiprocessing module under the hood
- Bypasses the GIL using separate processes.

why so many because each solve a issue with some trade off which we will later study about. so with ur needs choose any lib u want to use.


## GIL (global interpreter lock)
The **Global Interpreter Lock (GIL)** is a special lock used in **CPython** (the most popular Python interpreter) to make sure that only **one thread can execute Python bytecode at a time**.

Even if we create real OS-level threads, Python only interprets code from one thread at a time. It pauses the currently running thread, switches to another, and resumes each thread exactly where it left off.

---

### Diagram: Python vs C++ Threading
```text
# Python Threading (With GIL — takes turns)
|-(Thread1)-|             |-(Thread1)-|
             |-(Thread2)-|             |-(Thread2)-|

# C++ Threading (True Parallelism)
|----------- Thread 1 running full time -----------|
|----------- Thread 2 running full time -----------|
|----------- Thread 3 running full time -----------|
```

As you can see:
- Python **threads don't run in true parallel**, because the **GIL blocks other threads** from executing Python code.
- When Thread 1 is running, Thread 2 must wait, even though both **threads are real** and **managed by the OS**.
- The GIL enforces this, making sure that only one thread interprets Python bytecode at any moment.

---

### Is Python Threading Fast?
> Nope — threading in Python doesn’t increase speed for CPU-heavy tasks. its heavy in reality. because of regular gil management

When all threads are doing **CPU-heavy work**, Python threads take turns due to the GIL.
So instead of running in parallel, the threads are **effectively serialized**.
- **If each thread takes `t` seconds (doing heavy cpu task)**,
- **and you have `n` threads**
- **Then the total execution `time ≈ n * t` seconds**
- Threading does not reduce execution time for CPU-bound code.
- *in fact, it often adds overhead and runs slower than a single-threaded version.*

So:
- You don’t gain speed unless threads are waiting/blocking (like I/O, sleep, etc.).
- The only real benefit of Python threading is:
  > If Thread 1 is blocked, then Thread 2 can do something else.
- That’s why threading in Python isn’t good for heavy CPU work — it can actually decrease performance.

---

### But Why Does Python Even Have GIL?
> Why not just use threading.Lock() to manage memory access?
Great question! Here's the truth:\
The GIL exists because **Python’s memory system is not designed to be thread-safe internally**. Even if you protect your shared data with locks, Python itself still needs protection.

#### Problems GIL Prevents:
1. **Reference Counting**
   - Python tracks how many references point to each object.
   - If two threads update the same reference count at the same time → 💣 crash. GIL prevents this.
2. **Garbage Collection**
   - Python automatically finds and cleans up unused objects.
   - Without GIL, two threads might mutate memory during garbage collection.
3. **Non-Thread-Safe Internals**
   - Built-in types like list, dict, str are not safe to use across threads.
   - Adding internal locks would slow everything down and make Python more complex.

### Why Not Fix It Then?
- Changing Python’s memory model would break compatibility.
- There are millions of Python 3 libraries.
- Moving from Python 2 → 3 already caused huge problems. A “Python 4” with no GIL would be even harder to adopt.

> **So yeah, for now, we live with the GIL.**\
> Check out [this article](https://python.land/python-concurrency/the-python-gil) if you want a clean and simple explanation of the GIL.  
> And here's the [official docs](https://wiki.python.org/moin/GlobalInterpreterLock) if you're into deeper stuff.\
> Btw, there’s ongoing research to remove the GIL — let’s hope it shows up soon :)


## Why Do We Need Concurrency?

Why even use concurrency?

Because Python, by default, is **single-threaded** and **interpreted**, which means:

- One task runs at a time  
- Everything else has to **wait**  
- Even if you're just waiting for a response from the network — Python will sit and do nothing

This is fine for small scripts.  
But it breaks down fast when you try to:

- 🔄 Handle **multiple user requests** (e.g., a web server)
- 🖼️ Run **image processing** that blocks the main thread
- 🌐 Wait for **APIs, files, databases** — and block the whole flow

---

### Problem 1: One Task at a Time = Everything Waits

Imagine your web server gets a new request every second.  
If you handle them one by one in the **main thread**, they pile up fast.

It’s like taking a food order, cooking it yourself, delivering it, then finally returning to take the next order. 🐢 Slow.

Some tasks (like reading from disk or waiting on a network) **don’t even need CPU** — they’re just idle.  
But Python still blocks everything while waiting.

---

### Problem 2: Some Tasks Are CPU Monsters

Now imagine a task needs to **process an image** or run a **big calculation**.

It takes 10+ seconds, and during that time, the entire app is frozen.  
No new requests. No updates. Just stuck.

That’s because Python’s default model runs everything in **a single thread**, and CPU-heavy work takes over all of it.

---

### Problem 3: Some Tasks Just Wait

You’re calling an API or reading from a slow database.  
Your program isn’t doing real work — it’s just waiting.

But even then, the **main thread is blocked** doing *nothing*. That’s wasted time.

---

### Solution: Use the Right Tool for Each Problem

Python gives us **three main tools** to deal with these issues:

| Tool             | Best For                          |
|------------------|------------------------------------|
| `asyncio`        | I/O-bound tasks (waiting on things) |
| `threading`      | Light CPU or small blocking tasks  |
| `multiprocessing`| Heavy CPU-bound computation        |

Let’s break it down:

---

#### Solution 1: Asyncio

**Use when**: Your task **spends most of its time waiting** (I/O, APIs, DB, etc.)

`asyncio` creates a system where tasks pause with `await`, and control switches to another task while waiting.

It’s like saying:  
“You go wait for your network response — I’ll go handle something else in the meantime.”

Efficient use of one thread. Perfect for:
- Bots
- Web APIs
- File/network I/O
- Realtime systems that must stay responsive

---

#### Solution 2: Threading

**Use when**: You have **short CPU tasks** or tasks that block *briefly*

Python’s `threading` module creates real OS-level threads.  
But because of the **GIL**, only one thread runs Python bytecode at a time.

So threading is not truly parallel — but it’s still useful when:
- Tasks aren’t super CPU-heavy
- You’re calling `subprocess`, reading files, or doing disk I/O
- You want to keep your app responsive without async

---

#### Solution 3: Multiprocessing

**Use when**: You’re doing **heavy CPU-bound work** like:
- Image processing
- Machine learning
- Compression, encryption, hashing
- Data science and analytics

The `multiprocessing` module runs separate Python processes.  
Each process has its own:
- Interpreter
- GIL
- Memory space

So your code runs in **true parallel** across multiple CPU cores.  
They talk via queues/pipes — and Python handles the communication behind the scenes.

---

## Asyncio vs Threading vs Multiprocessing

| Feature            | Asyncio ⚡                               | Threading 🧵                             | Multiprocessing 🔥                   |
| ------------------ | --------------------------------------- | ---------------------------------------- | ------------------------------------ |
| GIL Limitation     | ❌ No blocking (1 thread, non-blocking) | ❗ GIL applies (only one runs at a time) | ✅ No GIL (separate processes)       |
| Concurrency Type   | Single-threaded, async/await            | Real OS threads (but serialized by GIL)  | Real processes with real parallelism |
| Best For           | I/O-bound (network, DB, APIs)           | Light CPU work, disk I/O, subprocesses   | CPU-bound (image, ML, encryption)    |
| Memory             | Shared memory                           | Shared memory                            | Isolated memory (uses pipes/queues)  |
| Analogy            | “While noodles boil, do homework.”      | “Kids taking turns with one pen.”        | “Each cook has their own kitchen.”   |
| Parallelism        | ❌ No                                   | ❌ No                                    | ✅ Yes                               |
| Speed (I/O vs CPU) | ✅ Very fast for I/O                    | 🚫 Okay for I/O, bad for CPU             | ✅ Great for CPU-heavy tasks         |

---

### 🔁 Visual Timeline

```text
[Asyncio]
||-- Task A --| (await)                  |
|             |-- Task B --| (await)     | -> single thread
|                          |-- Task C --||
(Tasks switch only when idle — perfect for I/O)

[Threading]
|-- Thread A --|              |-- Task A --|
               |-- Thread B --|
(Switch between threads — but GIL still active)

[Multiprocessing]
|-- Process A --------------------|
|-- Process B --------------------|
(Real parallel — runs on separate CPU cores)
```