# Asyncio Modules Index

> **Author** : Akhand Raj  
> **GitHub** : [@Akkiraj1234](https://github.com/Akkiraj1234)  
> **Date**   : 5 aug 2025  
> **Status** : ⏳ Ongoing

## Topics
1. [asyncio-queues](#asyncio-queues)
2. [asyncio-subprocess](#asyncio-subprocess)
3. [asyncio-locks](#asyncio-locks)
4. [asyncio-streams](#asyncio-streams)

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

### Index

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


## asyncio-locks
Asyncio locks — also called **synchronization primitives** — are used to coordinate access between multiple asynchronous tasks.
They are similar to primitives in the `threading` module, but with two key differences:

- Asyncio primitives **are not thread-safe** — use them only within the same event loop.
- Most of their methods **do not accept a `timeout` argument** — use `asyncio.wait_for()` if timeout behavior is needed.


### Index
| Class                                                                 | Definition                                                                                               | Key Methods                                                                                       |
| --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [`asyncio.Lock`](#asynciolock)                                        | lock that prevents multiple tasks from accessing shared resources at the same time.                      | `acquire()`, `release()`, `locked()`                                                              |
| [`asyncio.Event`](#asyncioevent)                                      | A simple flag for inter-task communication — one task can wait for an event to be set by another.        | `wait()`, `set()`, `clear()`, `is_set()`                                                          |
| [`asyncio.Condition(lock=None)`](#asyncioconditionlocknone)           | A condition variable that lets tasks wait until they are notified.                                       | `acquire()`, `wait()`, `wait_for(predicate)`, `notify()`, `notify_all()`, `release()`, `locked()` |
| [`asyncio.Semaphore(value=1)`](#asynciosemaphorevalue1)               | Limits access to a resource to a fixed number of concurrent tasks.                                       | `acquire()`, `release()`, `locked()`                                                              |
| [`asyncio.BoundedSemaphore(value=1)`](#asyncioboundedsemaphorevalue1) | Same as `Semaphore`, but raises an error if `release()` is called too many times.                        | `acquire()`, `release()`, `locked()`                                                              |
| [`asyncio.Barrier(parties)`](#asynciobarrierparties)                  | Lets a fixed number of tasks wait until all have reached the barrier, then continues together.           | `wait()`, `reset()`, `abort()`                                                                    |
| [`asyncio.BrokenBarrierError`](#asynciobrokenbarriererror)            | Raised when the barrier is broken (e.g. one of the waiting tasks fails).                                 | *Exception class — no methods*                                                                    |

---

### `asyncio.Lock`
A coroutine-friendly lock that ensures only one task can acquire it at a time. All other tasks trying to acquire it will pause and wait until it's released.

> ✅ Always use with `async with` to automatically acquire and release the lock.

#### Important Points
- Helps safely **access shared resources** one task at a time.
- The lock itself **doesn't own** the resource — it just controls **when a task gets to use it**.
- Other coroutines will wait in line, and resume when the lock is free.


#### Methods
| Method            | Description                                                                             |
| ----------------- | --------------------------------------------------------------------------------------- |
| `await acquire()` | Wait until the lock is available. The first coroutine that started waiting gets access. |
| `release()`       | Unlock the lock. Raises `RuntimeError` if already unlocked.                             |
| `locked()`        | Return `True` if the lock is currently held by any task.                                |

```python
import asyncio

lock = asyncio.Lock()

async def access_shared_resource():
    async with lock:
        print("🔒 Resource is locked and being accessed")
        await asyncio.sleep(1)
    print("🔓 Lock is released")

async def main():
    await asyncio.gather(
        access_shared_resource(),
        access_shared_resource()
    )

asyncio.run(main())
```
> You can create multiple asyncio.Lock() instances — each one is independent and controls access to its own resource.
> This means you don’t need to use a single lock for different resources. Instead, create separate locks, and tasks can access those resources in parallel without interference.

---

### `asyncio.Event`
An `asyncio.Event` is a **simple signaling mechanism** used to notify one or more coroutines that something has happened.
One task sets the event, and other tasks waiting for it will resume.

> Useful for coordinating tasks — e.g., "wait until download is ready" or "start when signal is set".


#### Important Points
- Initially unset (`False`), and all `wait()` calls will block until it's set.
- **Python 3.10**, the `loop` parameter has been removed.

#### Methods

| Method         | Description                                                                                   |
| -------------- | --------------------------------------------------------------------------------------------- |
| `await wait()` | Wait until the event is set. If already set, returns immediately.                             |
| `set()`        | Set the event to "True" — wakes up all tasks waiting on it.                                   |
| `clear()`      | Clear the event (set it to `False`) — future `wait()` calls will block again.                 |
| `is_set()`     | Return `True` if the event is set, `False` otherwise.                                         |

```python
import asyncio

event = asyncio.Event()

async def waiter(name):
    print(f"{name} is waiting for event...")
    await event.wait()
    print(f"{name} got the event!")

async def setter():
    print("Setter sleeping for 2 seconds...")
    await asyncio.sleep(2)
    print("Setter sets the event.")
    event.set()

async def main():
    await asyncio.gather(
        waiter("Task A"),
        waiter("Task B"),
        setter()
    )

asyncio.run(main())
```

---

### `asyncio.Condition(lock=None)`
`asyncio.Condition` is like a mix of `Event` and `Lock`.  
But what does that mean?

- An **`Event`** pauses all tasks until `.set()` or `.notify()` is called — then **all waiting tasks resume together**.
- A **`Lock`** allows only **one task at a time** to access a shared resource using a `with` or `async with` block.

With `Condition`, you get **both behaviors combined**:
- You can make tasks **wait** until they are **notified**.
- Once notified, each task will **re-acquire the lock one by one** — like a `Lock`.

You can use:
- `await cond.wait()` to wait for a notification.
- `await cond.wait_for(predicate)` to wait until a specific condition becomes true.

So `Condition` lets you coordinate **when** tasks should wake up, and also **control access** to the shared resource — **one at a time**.

#### Important Points

- Multiple `Condition` objects can share the same `Lock`.
- Since **Python 3.10**, the `loop` parameter has been removed.
- Prefer to use it as a **context manager**.

#### Parameter

- `lock`: *(optional)* A `Lock` object. If `None`, a new `Lock` is created automatically.

#### Methods

| Method                      | Description                                                                                                                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `await acquire()`           | Wait until the lock is available. The first coroutine that started waiting gets access.                                                                                          |
| `locked()`                  | Return `True` if the underlying lock is currently held.                                                                                                                          |
| `release()`                 | Release the underlying lock. If called when the lock is not acquired, raises `RuntimeError`.                                                                                     |
| `notify(n=1)`               | Wake up `n` tasks waiting on this condition. Must be called while holding the lock, otherwise raises `RuntimeError`.                                                             |
| `notify_all()`              | Wake up all tasks waiting on this condition. Must be called while holding the lock, otherwise raises `RuntimeError`.                                                             |
| `await wait()`              | Waits until notified. Temporarily releases the lock and blocks until a notification is received. Once notified, it re-acquires the lock before resuming. May wake up spuriously. |
| `await wait_for(predicate)` | Wait until the given `predicate()` returns predicate value. Automatically handles re-checking after wake-up. access lock one by one.                                             |

```python
import asyncio

shared_data = []
condition = asyncio.Condition()

async def consumer(name):
    async with condition:
        print(f"{name} is waiting for data...")
        await condition.wait()  # Wait until producer notifies
        print(f"{name} got data: {shared_data[-1]}")

async def producer():
    await asyncio.sleep(1)  # Simulate work
    async with condition:
        shared_data.append("🍎 Apple")
        print("Producer added an item and notifying...")
        condition.notify_all()  # Wake up all waiting consumers

async def main():
    consumers = [consumer(f"Consumer-{i}") for i in range(3)]
    await asyncio.gather(*(consumers + [producer()]))

asyncio.run(main())
```

---

### `asyncio.Semaphore(value=1)`  

A `Semaphore` is an **async context manager** that limits how many tasks can access a shared resource at once.  
If the limit is reached, extra tasks will **wait** until a running task calls `release()`.

#### Important Points
- If `value < 0`, raises `ValueError`.  
- Since **Python 3.10**, the `loop` parameter was removed.

#### Parameter
- `value`: *(default: 1)* — Max number of tasks allowed to access the resource at the same time.

#### Methods

| Method            | Description                                                                                 |
| ----------------- | ------------------------------------------------------------------------------------------- |
| `await acquire()` | If the internal counter > 0, decrement it and continue. Otherwise, wait until it's > 0.     |
| `locked()`        | Return `True` if the counter is 0 (i.e., no more tasks can acquire it right now).           |
| `release()`       | Increment the counter by 1. If any tasks are waiting, one of them will be resumed.          |

#### Example

```python
import asyncio

sem = asyncio.Semaphore(3)  # Only 3 tasks can access at once

async def worker(name):
    async with sem:
        print(f"{name} acquired")
        await asyncio.sleep(1)
    print(f"{name} released")

async def main():
    await asyncio.gather(*(worker(f"task-{i}") for i in range(6)))

asyncio.run(main())
```

---

### `asyncio.BoundedSemaphore(value=1)`  

Same as [`Semaphore`](#asynciosemaphorevalue1), but **safer**.  
Raises a `ValueError` if `release()` is called **more times than `acquire()`**.

#### Parameter
- `value`: *(default: 1)* — Max number of concurrent tasks. Must be ≥ 0.

#### Example
```python
import asyncio

sem = asyncio.BoundedSemaphore(1)

async def example():
    await sem.acquire()
    sem.release()
    sem.release()  # ❌ Raises ValueError

asyncio.run(example())
```

---

### `asyncio.Barrier(parties)`
A `Barrier` is an **async synchronization primitive** that blocks tasks until a given number (`parties`) are waiting on it.  
Once all required tasks reach the barrier (via `wait()` or `async with`), they **unblock together**.

> for example a fruit bucket can only be passed when its have 3 fruit , not 1,2 as its reach 3 its transfer and new bucket get in line
> - Introduced in **Python 3.11+**.
> - if any task got canceled its `-1` the `counter`

#### Parameters
- `parties`: Number of tasks that must call `wait()` to pass the barrier.

#### Attributes
- `n_waiting`: Number of tasks currently waiting.
- `broken`: `True` if the barrier is in a broken state (e.g., due to cancel/reset).

#### Methods

| Method          | Description                                                                                   |
|-----------------|-----------------------------------------------------------------------------------------------|
| `await wait()`  | Block until enough tasks arrive. Returns an `int` (0 to `parties-1`) unique per task.         |
| `await reset()` | Reset the barrier. All current waiting tasks will get `BrokenBarrierError`.                   |
| `await abort()` | Break the barrier. All waiting or future tasks raise `BrokenBarrierError` immediately.        |

```python
import asyncio

async def worker(barrier, name):
    print(f"{name} is waiting at the barrier...")
    try:
        await barrier.wait()
        print(f"{name} passed the barrier ✅")
    except asyncio.BrokenBarrierError:
        print(f"{name} couldn't pass the barrier ❌ (broken)")

async def main():
    barrier = asyncio.Barrier(3)  # Need 3 tasks

    # Only starting 2 tasks
    t1 = asyncio.create_task(worker(barrier, "Task-1"))
    t2 = asyncio.create_task(worker(barrier, "Task-2"))

    await asyncio.sleep(0.5)  # Give them time to reach barrier

    print("Main is aborting the barrier!")
    await barrier.abort()     # Cancel the barrier

    await t1
    await t2

asyncio.run(main())
```

---

### `asyncio.BrokenBarrierError`
`Exception`
This exception, a **subclass** of `RuntimeError`, is raised when the Barrier object is **reset** or **broken**.

---

## asyncio-streams


## more..
1. asyncio.protocols
2. asyncio.transports
3. asyncio.events
4. asyncio.trsock