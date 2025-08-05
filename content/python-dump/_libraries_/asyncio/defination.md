# Asyncio Programming Definition

> **Author** : Akhand Raj  
> **GitHub** : [@Akkiraj1234](https://github.com/Akkiraj1234)  
> **Date**   : 13 July 2025  
> **Status** : ⏳ Ongoing
```python
import asyncio # build in library no pip required but in case its missing do `sudo apt install python-asyncio`
```
---

## Topics
1. [Basics](#basics)
2. [Things U should know about asyncio](#things-u-should-know-about-asyncio)
3. [Event Loop]


---

## Basics

`asyncio` is a Python standard library used to write **asynchronous**, **non-blocking**, and **concurrent** programs using `async` and `await` keyword.  
It's mostly used for **I/O tasks** like APIs, networking, and file access — places **where code often waits**.

- **`async`**: A Python keyword used to mark certain code as asynchronous. Most commonly used with `def` to define a **coroutine** — a special kind of function that can be **paused (with `await`) and resumed later at any point during execution**. that makes it perfect for asyncio.


- **`await`**:A Python keyword used to **run** an object that is **awaitable** — like a coroutine, Task, or Future. When you `await` something, it gets **sent to the event loop**, which runs it and pauses your code until it's done at any point during execution. — without blocking the rest of your program.

---

**example:**

```python
async def get_data():
    return "hello"

async def main():
    coro = get_data()
    data = await coro
    print(data)

asyncio.run(main())  # main() returns a coroutine object
```

- First, we define a coroutine `get_data()` using `async def`. This doesn't run the function immediately — it creates a **coroutine** its like a function.
- Then we define another coroutine `main()`. In asyncio, you always need one **main coroutine** that acts as the entry point.
- Inside `main()`, we call `get_data()` and store the result in `coro`. Since `get_data()` is a coroutine, it just returns a **coroutine object**, not the actual result.
- We then `await coro`, which sends it to the **event loop** — the heart of asyncio that schedules and runs tasks. The loop runs it when it's the right time (based on traffic, I/O, etc.), and gives us the return value.
- The result (`"hello"`) is stored in `data` and printed.
- Finally, we run the `main()` coroutine using `asyncio.run()`, which creates a new **event loop**, starts the coroutine, and manages everything behind the scenes.

--- 

## Things U should know about asyncio.

- asyncio uses weakref so object might dispear if u dont hold refreace.
- alway cover ur task in try/except with `asyncio.CancelledError` so u can do cleanup.
- alway re-raise `asyncio.CancelledError` after catching the error.

---

## Event Loop
> **The event loop is the engine of `asyncio`.**  
> It drives all coroutines: schedules, pauses, resumes, and coordinates everything async.

### ✅ High-level usage (recommended):
- Use `asyncio.run()`, `create_task()`, and `await` for 99% of use cases.
- Avoid touching the event loop directly unless you're writing a **framework**, **plugin sandbox**, or low-level system.

### 🧪 Common event loop functions:
```python
asyncio.get_running_loop()      # Current loop inside coroutine
asyncio.get_event_loop()        # Current loop (or create if outside, <3.12)
asyncio.new_event_loop()        # Create a fresh loop (e.g. in thread)
asyncio.set_event_loop(loop)    # Assign loop to current thread
```

---

### 🔍 Advanced event loop capabilities (if you're building a system):
- Schedule callbacks and timers
- Create and manage tasks/futures manually
- TCP/UDP connections and servers
- Work with raw sockets and pipes
- Transfer files and watch file descriptors
- Run subprocesses (see below)
- Handle UNIX signals
- Set debug mode
- Implement custom loop policies or loop classes

---

## Coroutines and Tasks
In asyncio, there are three types of awaitables that can be used with the await keyword:
- `coroutines`
- `Tasks`
- `Future`
> Awaitables: an object is an awaitable object if it can be used in an `await`

### coroutines
A coroutine is a function declared using `async def`, Calling a coroutine function like `main()` does not run it immediately. It returns a `coroutine object`.
To actually run it, you must use await, or schedule it with a task.
- Coroutines are **pauseable** and **resumable**, which means they can suspend execution (e.g., during I/O) and resume later.
- await wait for it to finish before moving ahead

### Tasks
A Task is a wrapper for a coroutine that schedules it to run concurrently.
- Created using asyncio.create_task(coro) or loop.create_task(coro).
- when we await it , its start to run in background await don't wait for it to finish and read ahead
> ✅ Use Tasks to run coroutines concurrently and improve performance.

### Future
A Future is a low-level awaitable object that represents a value that will be available in the future.
> Awaiting a future means your coroutine will pause until some other part of the program resolves or sets the result of that future.
Normally, you do not create Future objects manually in application-level code.
They're mostly used under the hood by asyncio and libraries built on top of it.




<!-- 
--- 
> 🧠 **Remember**: Calling an async function without await just returns a coroutine object — it doesn't actually run.
> ```python
> async def hello():
>     print("I am async code")
> 
> hello()  # ❌ Does NOT run
> # Output: <coroutine object hello at 0x722da904c4c0>
> ```
> `<coroutine object hello at 0x722da904c4c0>`\
> a coroutine object it will run only when u await it with `await hello()` -->



### things i need to add
1. stack frame in loop
2. how to handle sigint keybord interpurpt etc.
   2. First Ctrl+C:
      - Cancels the main coroutine via `.cancel()`
      - Inside your coroutine, `asyncio.CancelledError` is raised
      - You can handle cleanup there
   1. Second Ctrl+C:
      - Immediately raises `KeyboardInterrupt` and exits forcefully
