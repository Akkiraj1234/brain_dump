# Asyncio Modules Index

> **Author** : Akhand Raj  
> **GitHub** : [@Akkiraj1234](https://github.com/Akkiraj1234)  
> **Date**   : 5 aug 2025  
> **Status** : ⏳ Ongoing

## Topics
1. [asyncio-queues](#asyncio-queues)
2. [asyncio-subprocess](#asyncio-subprocess)
3. [asyncio-locks]
4. [asyncio-streams]
5. [asyncio-exceptions]
6. [more]

---

## asyncio-queues
A **queue** is a data structure where items are added at one end and removed from the other — first-in, first-out (FIFO).  
`asyncio-queues` are awaitable, non-blocking classes used to manage communication between coroutines.  
They allow async tasks to safely pass data to each other — useful in pipelines, background workers, and producer-consumer systems.  
Unlike `queue.Queue`, these queues are designed for a **single event loop** and are **not thread-safe**,  
because `asyncio` assumes all coroutines run in the same thread (so no locking is needed).

| Class                                                               | Definition                      | Methods                                                           |
|---------------------------------------------------------------------|---------------------------------|-------------------------------------------------------------------|
| [`asyncio.Queue(maxsize=0)`](#asyncioqueuemaxsize0)                 | FIFO queue for async tasks.     | `put()`, `get()`, `task_done()`, `join()`, `shutdown()`, ...      |
| [`asyncio.PriorityQueue(maxsize=0)`](#asynciopriorityqueuemaxsize0) | Priority-based async queue.     | Inherits all from `Queue`                                         |
| [`asyncio.LifoQueue(maxsize=0)`](#asynciolifoqueuemaxsize0)         | Stack-based async queue (LIFO). | Inherits all from `Queue`                                         |

---

### `asyncio.Queue(maxsize=0)`
A **first-in, first-out (FIFO)** queue designed for asynchronous code using `asyncio`.  
It works like `queue.Queue`, but is specifically built for async tasks.

- If `maxsize ≤ 0`, the queue is unbounded.
- If `maxsize > 0`, `await put()` blocks when the queue is full until space becomes available (i.e., an item is removed by `get()`).
- **Not thread-safe** — intended for use within a single async event loop.
- From **Python 3.13**, the queue supports **shutdown mode**.

#### Parameters

- **`maxsize`**: Maximum number of items allowed in the queue.  
- **`loop`** *(deprecated)*: Event loop to use (**removed in Python 3.10**).

#### Methods

| Method                       | Description |
|-----------------------------|-------------|
| `maxsize`                   | Maximum number of items allowed in the queue. |
| `empty()`                   | Returns `True` if the queue is empty. |
| `full()`                    | Returns `True` if the queue is full (only when `maxsize > 0`). |
| `async get()`               | Awaitable. Waits until an item is available and returns it. Raises `QueueShutDown` if the queue is shut down and empty. |
| `async put(item)`           | Awaitable. Waits until space is available to add the item. Raises `QueueShutDown` if the queue is shut down. |
| `async join()`              | Awaitable. Waits until all unfinished tasks are marked as done. |
| `qsize()`                   | Returns the current number of items in the queue. |
| `get_nowait()`              | Immediately returns an item or raises `QueueEmpty` if none are available. |
| `put_nowait(item)`          | Immediately puts an item or raises `QueueFull` if the queue is full. |
| `task_done()`               | Signals completion of a task taken from the queue. Raises `ValueError` if called more times than there were items put into the queue. |
| `shutdown(immediate=False)` | Puts the queue into shutdown mode. <br/>- Stops all future `put()` calls. and raise `QueueShutdown` if called. <br/>- If `immediate=False`: allows already added items to be processed normally using `get()` + `task_done()`. <br/>- If `immediate=True`: the queue is drained immediately, blocked `put()`/`get()` calls are cancelled, and `join()` unblocks even if some tasks were not processed. Use with caution. |

```python
import asyncio

async def producer(queue):
    for i in range(3):
        await queue.put(i)
        print(f"Produced {i}")
    await queue.join()     # Wait until all items are processed
    queue.shutdown()       # Shut down after done

async def consumer(queue):
    while True:
        try:
            item = await queue.get()
        except asyncio.QueueShutDown:
            break
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    consumer_task = asyncio.create_task(consumer(queue))  # ✅ Run consumer independently
    await producer(queue)                                 # Run producer
    await consumer_task                                   # Wait for consumer to finish

asyncio.run(main())
```

---

### `asyncio.PriorityQueue(maxsize=0)`

A **priority-based queue** for asynchronous tasks.  
Retrieves items in **ascending order** of priority (lowest first).

- Items must be ordered (typically tuples like `(priority, data)`).
- All methods (e.g., `put`, `get`, `join`, `task_done`) are the same as `Queue`.
> Behaves exactly like [`asyncio.Queue`](#asyncioqueuemaxsize0), but uses a **heap** internally.

```python
import asyncio

async def main():
    queue = asyncio.PriorityQueue()
    await queue.put((2, "low"))
    await queue.put((1, "high"))
    await queue.put((3, "very low"))

    while not queue.empty():
        priority, value = await queue.get()
        print(value)
        queue.task_done()

    await queue.join()

asyncio.run(main())
```

---

### `asyncio.LifoQueue(maxsize=0)`

A **stack-like async queue** (Last-In, First-Out).

- The most recently added item is retrieved **first**.
- All methods (e.g., `put`, `get`, `join`, `task_done`) are the same as `Queue`.
> Behaves exactly like [`asyncio.Queue`](#asyncioqueuemaxsize0), but items come out in reverse order.

```python
import asyncio

async def main():
    queue = asyncio.LifoQueue()
    await queue.put("first")
    await queue.put("second")
    await queue.put("third")

    while not queue.empty():
        item = await queue.get()
        print(item)
        queue.task_done()

    await queue.join()

asyncio.run(main())
```

---

#### 🧠 Summary

| Queue Type         | Order     | Internal Structure | Use Case                        |
|--------------------|-----------|--------------------|---------------------------------|
| `Queue`            | FIFO      | List               | Most async producer-consumer    |
| `PriorityQueue`    | Priority  | Heap               | Task scheduling by priority     |
| `LifoQueue`        | LIFO      | List (reversed)    | Stack-like structures           |

---

## asyncio-subprocess

The `asyncio.subprocess` module allows you to **run external programs asynchronously** using coroutines — such as shell commands, binaries, or scripts — without blocking the main event loop.

These subprocesses integrate with `asyncio`’s I/O system using `StreamReader` and `StreamWriter` from `asyncio.streams`.

> ⚠️ **Not thread-safe**: Like most asyncio components, `asyncio.subprocess` is designed to work within a single thread and event loop. Use in multi-threaded programs may lead to race conditions or undefined behavior.

### 🔧 Constants

- **`asyncio.subprocess.PIPE`**  
  Used for `stdin`, `stdout`, or `stderr`.  
  - If passed to `stdin`, `Process.stdin` becomes a `StreamWriter`.  
  - If passed to `stdout` or `stderr`, they become `StreamReader` objects.

- **`asyncio.subprocess.STDOUT`**  
  Can only be passed to `stderr`.  
  - It redirects standard error (errors) into standard output — both go to the same place.

- **`asyncio.subprocess.DEVNULL`**  
  Silently ignores input/output.  
  - Like sending/receiving data from a black hole (`/dev/null`).

---

> 💡 **Beginner-Friendly Explanation**
>
> If you don't pass any value to `stdin`, `stdout`, or `stderr`, their default is `None`.  
> This means:
> 
> - `stdin` will take input **directly from the terminal**.
> - `stdout` will print output **to the terminal**.
> - `stderr` will show errors **in the terminal**.
>
> Now, if you use `asyncio.subprocess.PIPE` instead:
>
> - For `stdin`, you get a `StreamWriter`, which lets you **send input from code** instead of the terminal.
> - For `stdout` and `stderr`, you get `StreamReader` objects, so you can **read output and errors from code**, not from the screen.
>
> This is useful when you want full control over the subprocess — like sending custom input or custom bytes, capturing output or reading certain bytes, or logging errors.
>
> `STDOUT` is special — you can pass it **only to `stderr`**. It merges errors into output, so both go into `stdout`.  
> (Good if you want to read all output in one stream.)
>
> `DEVNULL` means: "Don't show or read anything."  
> - If used in `stdout`, output is ignored.
> - If used in `stdin`, it won’t accept any input.
> - If used in `stderr`, errors are discarded.
>
> Simple as that — you're just telling Python **where the subprocess should get input and where to send output or errors.**

---

### 📋 Index

| Function / Class                                                                 | Description                                                     | Key Methods / Attributes                                       |
|----------------------------------------------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------|
| [`asyncio.create_subprocess_exec(...)`](#asynciocreate_subprocess_execprogram-args-stdinnone-stdoutnone-stderrnone-limitnone-kwds) | Launch an external program without a shell (safer, preferred).  | `communicate()`, `wait()`, `stdin`, `stdout`, `stderr`         |
| [`asyncio.create_subprocess_shell(...)`](#asynciocreate_subprocess_shellcmd-stdinnone-stdoutnone-stderrnone-limitnone-kwds)        | Launch a command through the shell (`/bin/sh`).                 | Same as above                                                  |
| [`asyncio.subprocess.Process`](#asynciosubprocessprocess)                        | Represents the running process object and provides control.     | `pid`, `returncode`, `kill()`, `terminate()`, `communicate()`  |

---

### `asyncio.create_subprocess_exec(program, *args, stdin=None, stdout=None, stderr=None, limit=None, **kwds)`
Launches an **external program or binary** asynchronously and **Returns** a `Process` instance.  
Does **not** use the shell — safer and faster for direct command execution.

### Parameters

- `program`: Name/path of the executable (e.g. `"python"`, `"/usr/bin/ffmpeg"`).
- `*args`: Command-line arguments to pass after the program (e.g. `"main.py"`, `"-v"`).
- `stdin`: (optional) Input stream, Accepts: `None` (default), `asyncio.subprocess.PIPE`, `DEVNULL`, or a file-like object.
- `stdout`: (optional) Output stream, Accepts: same options as `stdin`.
- `stderr`: (optional) Error stream, Accepts: same options as `stdin`. You can also pass `STDOUT`.
- `limit`: (optional) Buffer size for `StreamReader` (used in `stdout` and `stderr` if `PIPE` is used), Defaults to `asyncio.streams._DEFAULT_LIMIT`.

```python
import asyncio

async def main():
    # Run: python -c "print('Hi')"
    process = await asyncio.create_subprocess_exec(
        "python", "-c", "print('Hi')",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    out, err = await process.communicate()
    print("Output:", out.decode())
    print("Error:", err.decode())

asyncio.run(main())
```

---

### `asyncio.create_subprocess_shell(cmd, stdin=None, stdout=None, stderr=None, limit=None, **kwds)`
Runs a **shell command string** asynchronously — like you'd type in a terminal (`"ls -la | grep py"`).  
**Returns** a `Process` instance.  
> Unlike `create_subprocess_exec()`, this one uses a shell — so it supports pipes (`|`), wildcards (`*`), redirection (`>`, `<`), etc.

### Parameters

- `cmd`: The shell command as a single string (e.g. `"python -c 'print(42)'"`).
- `stdin`, `stdout`, `stderr`, `limit`, `**kwds`: Same as in [`create_subprocess_exec()`](#asyncio_create_subprocess_exec).

### ⚠️ Caution:
Avoid passing user input directly — shell commands are prone to **injection attacks**.  
Use `create_subprocess_exec()` if you're not using shell features (it's safer + faster).

```python
import asyncio

async def main():
    process = await asyncio.create_subprocess_shell(
        "echo Hello && echo Error >&2",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    out, err = await process.communicate()
    print("Out:", out.decode())
    print("Err:", err.decode())

asyncio.run(main())
```

---


### `asyncio.subprocess.Process`

A `Process` object used to manage and interact with a running subprocess.
It works similar to `subprocess.Popen`, but with a few important differences:

- No `.poll()` method — use `await proc.wait()` instead.
- No `universal_newlines` — all I/O is in **`bytes`**, not `str`.
- Not thread-safe — interact only from the **same event loop**.
- Fully **asynchronous** and coroutine-friendly (non-blocking).

> 📚 For deeper understanding, please check the official docs:  
> [asyncio.subprocess.Process – Python Docs](https://docs.python.org/3/library/asyncio-subprocess.html#asyncio.subprocess.Process)

---

#### Attributes

- `stdin`: A `StreamWriter` to send input (if `stdin=PIPE`), else `None`.
- `stdout`: A `StreamReader` to read output (if `stdout=PIPE`), else `None`.
- `stderr`: A `StreamReader` to read errors (if `stderr=PIPE`), else `None`.
- `pid`: Process ID of the spawned child process.
- `returncode`: Exit code of the process, `None` if still running, On **POSIX**, `-N` means the process was terminated by signal N.

> ⚠️ **Important:** It's safer to use `communicate()` to avoid deadlocks caused by full pipe buffers when writing/reading large outputs.

#### Methods
| Method                                  | Description                                                                 |
| --------------------------------------- | --------------------------------------------------------------------------- |
| `await process.wait()`                  | Waits for the process to exit. Sets `.returncode`. <br>⚠️ If using `PIPE` for `stdin`, `stdout`, or `stderr`, large I/O may block unless you use `communicate()`. |
| `await process.communicate(input=None)` | Sends `input` (as `bytes`) to stdin (if set), closes stdin, reads all output from `stdout` and `stderr` till EOF, and waits for process to exit. Returns `(stdout_data, stderr_data)`. <br>🔒 Avoids common deadlocks. |
| `process.send_signal(signal)`           | Sends a signal (like `signal.SIGTERM`) to the process.                      |
| `process.terminate()`                   | Sends `SIGTERM` (on POSIX) or calls `TerminateProcess()` (on Windows).      |
| `process.kill()`                        | Sends `SIGKILL` (POSIX) or forcefully kills the process on Windows.         |

---

#### ❓ What if you don't want to use `communicate()`?

You can manually read/write using the `stdin`, `stdout`, and `stderr` streams if you want more control over the subprocess I/O.

> ⚠️ **But be careful!**  
> If you’re not careful, your program can **deadlock** — get stuck waiting forever.

To avoid deadlocks:

- ✅ Always call `await proc.stdin.drain()` after `proc.stdin.write(...)`  
  → this flushes the write buffer, ensuring data is sent to the subprocess.
- ✅ Always **read from `stdout` and `stderr`** while the process runs  
  → if you don’t, the subprocess might block while trying to write output.

---

#### Manual example (write + drain + read)

```python
import asyncio

async def main():
    proc = await asyncio.create_subprocess_exec(
        "python", "-c", "print(input())",
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE
    )

    # Write to subprocess
    proc.stdin.write(b"hello from Akki\n")
    await proc.stdin.drain()  # flush buffer to avoid blocking
    proc.stdin.close()

    # Read output
    line = await proc.stdout.readline()
    print("Subprocess output:", line.decode().strip())

    await proc.wait()

asyncio.run(main())
```

#### Deadlocks Explained (in simple words)
A **deadlock** can happen when:

- You're writing to **stdin**, but the buffer fills up
- Or the subprocess is writing to **stdout**, but you're not reading it
- And both processes get stuck waiting for each other to do something.

#### How `communicate()` avoids this
`process.communicate()` does **all 3 things safely**:

- Sends input (if provided)
- Closes stdin
- Reads from stdout and stderr until EOF
- Waits for the process to finish

This prevents any side from getting stuck.

> So, for most use cases:
> 🔐 Just use await process.communicate(...) — it’s safe.
> but `communicate()` is simple but limited. If you need **interactive I/O**, real-time control, or frame-precise reading/writing (like `ffmpeg` pipelines), use `stdin.write()`, `stdout.read()`, and `await writer.drain()` manually.

#### ✅ Minimal example with communicate()

```python
import asyncio

async def main():
    proc = await asyncio.create_subprocess_exec(
        "python", "-c", "print('Hello from subprocess')",
        stdout=asyncio.subprocess.PIPE
    )
    out, _ = await proc.communicate()
    print(out.decode().strip())  # Output: Hello from subprocess

asyncio.run(main())
```
---

#### 🧠 Summary

| If you're doing...        | Do this to stay safe             |
| ------------------------- | -------------------------------- |
| Writing to `stdin`        | ✅ Use `await proc.stdin.drain()` |
| Reading from `stdout`     | ✅ Use `await proc.stdout.read()` |
| Wanting full I/O + safety | ✅ Use `await proc.communicate()` |

> Deadlocks mostly happen when the subprocess pauses, waiting for you to read or write, and you’re not doing it right. communicate() is safe because it handles everything.





## more..
1. asyncio.protocols
2. asyncio.transports
3. asyncio.events
4. asyncio.trsock