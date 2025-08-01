# Asyncio Functions and classes

> **Author** : Akhand Raj  
> **GitHub** : [@Akkiraj1234](https://github.com/Akkiraj1234)  
> **Date**   : 1 Aug 2025  
> **Status** : Completed

---

## Topics
1. [Function Index](#function-index)
2. [Class Index](#class-index)
3. [Error Index](#error-index)
4. [Module Index](./module.md) 

---

## Function Index

| Function                                                                                   | Definition                                                                                 |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| [`asyncio.run(main, *, debug=None, loop_factory=None)`](#asynciorunmain--debugnone-loop_factorynone) | Create event loop, run a coroutine, close the loop.                                        |
| [`asyncio.create_task(coro, *, name=None, context=None)`](#asynciocreate_taskcoro--namenone-contextnone) | Start an asyncio Task and return it.                                                       |
| [`asyncio.current_task(loop=None)`](#asynciocurrent_taskloopnone)                          | Return the currently running Task instance, or `None` if no task is running.              |
| [`asyncio.all_tasks(loop=None)`](#asyncioall_tasksloopnone)                                | Return all tasks that are not yet finished for an event loop.                             |
| [`asyncio.iscoroutine(obj)`](#asyncioiscoroutineobj)                                       | Check if an object is a coroutine object (already called).                                |
| [`asyncio.sleep(delay, result=None)`](#asynciosleepdelay-resultnone)                       | Sleep for a number of seconds asynchronously.                                              |
| [`asyncio.gather(*aws, return_exceptions=False)`](#asynciogatheraws-return_exceptionsfalse) | Schedule and wait for multiple awaitables concurrently.                                   | 
| [`asyncio.wait_for(aw, timeout)`](#asynciowait_foraw-timeout)                              | Wait for an awaitable to finish, but with a timeout.                                      |
| [`asyncio.shield(aw)`](#asyncioshieldaw)                                                   | Protect an awaitable from being cancelled.                                                |
| [`asyncio.wait(aws, *, timeout=None, return_when=asyncio.ALL_COMPLETED)`](#asynciowaitaws--timeoutnone-return_whenasyncioall_completed) | Wait for tasks with flexible completion rules.                                            |
| [`asyncio.timeout(delay)`](#asynciotimeoutdelay)                                           | A context manager to set deadline using relative time in seconds.                         |
| [`asyncio.timeout_at(when)`](#asynciotimeout_atwhen)                                       | A context manager to set deadline using absolute loop time.                               |
| [`asyncio.to_thread(func, /, *args, **kwargs)`](#asyncioto_threadfunc--args-kwargs)        | Run blocking code in a separate thread safely inside asyncio.                             |
| [`asyncio.run_coroutine_threadsafe(coro, loop)`](#asynciorun_coroutine_threadsafecoro-loop) | Run an asyncio coroutine from another thread, safely and synchronously.                   |
| [`asyncio.as_completed(aws, *, timeout=None)`](#asyncioas_completedaws--timeoutnone)       | Yield awaitables as they complete, in completion order.                                   |
| [`asyncio.eager_task_factory(loop, coro, *, name=None, context=None)`](#asyncioeager_task_factoryloop-coro--namenone-contextnone) | Task factory that runs coroutine immediately if no `await` is used.                       |
| [`asyncio.create_eager_task_factory(custom_task_constructor)`](#asynciocreate_eager_task_factorycustom_task_constructor) | Create a custom eager task factory using your own constructor.                            |


## Class index
| Class                                                                                                                                              | Definition                                                              | Methods                                                           |
|----------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|-------------------------------------------------------------------|
| [`asyncio.Runner(*, debug=None, loop_factory=None)`](#asynciorunner-debugnone-loop_factorynone)                                                    | A context manager for running multiple async calls in the same loop.    | `run(coro, *, context=None)`, `get_loop()`, `close()`              |
| [`asyncio.Timeout(when: Optional[float])`](#asynciotimeoutwhen-optionalfloat)                                                                      | A context manager for setting an absolute timeout on a coroutine.       | `when()`, `reschedule(when)`, `expired()`                         |
| [`asyncio.Task(coro, *, loop=None, name=None, context=None, eager_start=False)`](#asynciotaskcoro--loopnone-namenone-contextnone-eager_startfalse) | Represents an asynchronous task created from a coroutine.               | `cancel(msg=None)`, `done()`, `result()`, `exception()`, ...       |
| [`asyncio.TaskGroup(*, loop=None, name=None)`](#asynciotaskgroup-loopnone-namenone)                                                                | A context manager for running and waiting on multiple tasks as a group. | `create_task(coro, *, name=None)`, `cancel_scope()`, ...           |


## Error Index
| Error                               | Definition                                                                                                                                                                                                                                             |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `asyncio.CancelledError`            | Raised when a task is cancelled. If caught, it **must be re-raised** to ensure proper cancellation behavior.                                                                                                                                           |
| `asyncio.TimeoutError`              | *(Deprecated)* Alias of the built-in `TimeoutError`. Raised when an operation exceeds its allotted time.                                                                                                                                               |
| `asyncio.InvalidStateError`         | Raised when an operation is performed on a `Task` or `Future` that is in an invalid state (e.g., setting a result twice).                                                                                                                              |
| `asyncio.IncompleteReadError`       | Raised when a read operation on a stream ends before the expected number of bytes is received. Subclass of `EOFError`. <br/>Has attributes: <br/>• `expected` – total number of bytes expected (int) <br/>• `partial` – bytes read before stream ended |
| `asyncio.LimitOverrunError`         | Raised when the buffer size is exceeded while searching for a separator. <br/>Has attribute: <br/>• `consumed` – number of bytes that need to be skipped or discarded                                                                                  |
| `asyncio.SendfileNotAvailableError` | Raised when the system does not support the `sendfile` syscall for a given file or socket. Subclass of `RuntimeError`.                                                                                                                                 |
| `KeyboardInterrupt`                 | Raised when the user sends an interrupt signal (usually `Ctrl+C`). Used to gracefully stop the program.                                                                                                                                                |
| `SystemExit`                        | Raised when `sys.exit()` is called. Used to exit from the program with a given status.                                                                                                                                                                 |



---

## `asyncio.run(main, *, debug=None, loop_factory=None)`

This function runs the given **coroutine** and manages everything — like setting up and closing the event loop.

- It's the main **entry point** for any asyncio program.
- Can only be called if no other event loop is running in the same thread.
- After your coroutine finishes, any background tasks are given **5 minutes** to shut down. If they don’t, a warning is shown and they’re stopped.
- after `3.11` its uses `asyncio.Runner` class to manage the function.

### Parameters

- `main`: the coroutine to run.
- `debug`: run loop in debug mode (optional).
- `loop_factory`: use a custom event loop, like `uvloop.new_event_loop()` (optional).

```python
asyncio.run(main())
```

---

## `asyncio.create_task(coro, *, name=None, context=None)`
Creates a **Task** from the given coroutine and **Schedules it to run in the current event loop** the time its created.
**Return** a `Task` object, and **Raises** a `RuntimeError` if there is no running event loop.

### Parameters
- `coro`: The coroutine function you want to run.
- `name`: (optional) A name for the task if None created by `Task.set_name()`
- `context`: (optional) A `contextvars.Context` object to pass custom variable scope into the task.

```python
async def do_work():
    await some_work()

task = asyncio.create_task(do_work())  # Runs in background
```

---

## `asyncio.current_task(loop=None)`
Returns the **currently running Task** object in the given event loop — or `None` if no task is running.

### Parameters
- `loop`: (optional) The event loop to check.  
  If not given, it uses `asyncio.get_event_loop()` to get the current loop.

```python
task = asyncio.current_task()
```

---

## `asyncio.all_tasks(loop=None)`
Returns a **set of all active (unfinished) Task objects** in the given event loop.

### Parameters
- `loop`: (optional) The event loop to check.  
  If not provided, it uses `asyncio.get_running_loop()` to fetch the current one.

```python 
tasks = asyncio.all_tasks()
```

---

## `asyncio.iscoroutine(obj)`
Returns **True** if the object is a coroutine object (not a coroutine function). It does not return True for regular functions or async def functions until they’re called.

### Parameters
- `obj`: The object you want to check.

```python
async def some_async(): pass

iscoroutine(some_async)       # False
iscoroutine(some_async())     # True
```

---

## `asyncio.sleep(delay, result=None)`
**`awaitable`**\
Pauses the current coroutine for the given number of seconds — without blocking the whole program.  
This allows other async tasks to run during that time.
> If you use await asyncio.sleep(0), it won’t sleep. Instead, it just gives the event loop a chance to let other tasks run. This is helpful when you’re doing long work and want to stay cooperative.

### Parameters
- `delay`: How many seconds to wait (can be a float).
- `result`: (Optional) The value to return after sleeping.

```python
await asyncio.sleep(0)  
```

---

## `asyncio.gather(*aws, return_exceptions=False)`
**`awaitable`**\
Runs all the given awaitable objects **concurrently** (it automatically wraps them into Tasks).
If all awaitables complete successfully without errors, it returns a list of their results in the **same order** as provided.

- If an error happens and `return_exceptions = False`:  
  The exception is **raised immediately** to the coroutine that's currently awaiting `gather()`, and no result is returned. and **The rest of the coroutines will still run unless cancelled manually**.

- If an error happens and `return_exceptions = True`:  
  The exception is **captured** and returned in the result list, in the position of the coroutine that failed.  
  Other tasks continue running normally.

- If `gather()` itself is **cancelled**, then **all** the awaitables are cancelled.

- If any task/future inside `gather()` is cancelled individually, a `CancelledError` is raised for that task.  
  The final result will still be returned (even if `return_exceptions` is `False`).

### Parameters
- `*aws`: List of **awaitable** objects (coroutines, Tasks, or Futures).
- `return_exceptions`: If `True`, return exceptions instead of raising them. Default is `False`.

```python
async def main():
    results = await asyncio.gather(say_hi(), say_bye())
    print(results)  # ➜ ['Hi', 'Bye']
```

---

## `asyncio.wait_for(aw, timeout)`
**`awaitable`**\

Waits for the given awaitable (`aw`) to finish within a time limit (`timeout`). return output.

- If `timeout=None`, it waits as long as needed.
- If the task takes longer than `timeout`, it’s **cancelled** and raises `TimeoutError`.
- It waits for the task to finish cancelling, so actual wait time might be slightly longer.
- If the coroutine **catches its cancellation** and returns a value, that value is returned instead of an error.
- If the parent task is cancelled, the inner awaited task is also cancelled.

✅ Good for setting timeouts for long tasks.

### Parameters
- `aw`: The coroutine or future to wait for.
- `timeout`: How long to wait in seconds (`int`, `float`, or `None`).

```python 
async def main():
    try:
        result = await asyncio.wait_for(slow_task(), timeout=1)
        print("Result:", result)
    except asyncio.TimeoutError:
        print("⏰ Timed out!")
```

---

## `asyncio.shield(aw)`
**`awaitable`**\

Protects an awaitable (`aw`) from being cancelled — even if the outer task gets cancelled.  
(Still raises `CancelledError` at the *caller*, but not *inside* the task.)

- If the outer coroutine is cancelled (e.g. user presses Ctrl+C), shield() raises CancelledError, but the inner coroutine keeps running safely.
- From the inner coroutine’s view, nothing happened — it doesn’t get cancelled.

> However, if the task cancels itself, shield() can’t stop that. and shield also got cancelled

### Parameters
- `aw`: the awaitable its takes

```python
task = asyncio.create_task(something())
    try:
        res = await shield(task)
    except CancelledError:
        res = None
```

---

## `asyncio.wait(aws, *, timeout=None, return_when=asyncio.ALL_COMPLETED)` 
**`awaitable`**

Runs multiple Tasks or Futures concurrently and waits based on the condition provided.
It returns two sets: `(done, pending)` — completed tasks and those still running.

> 🚫 It does **NOT** raise `TimeoutError`.  
> 🟡 Pending tasks are **not cancelled**, they keep running unless you cancel them manually.

### Parameters
- `aws`: A list/set of awaitables (Task or Future).
- `timeout`: Time to wait in seconds (`int`, `float`, or `None`). If `None`, wait forever.
- `return_when`: Condition that decides **when** to return:
  - `asyncio.ALL_COMPLETED`: Wait until all tasks are done or cancelled.
  - `asyncio.FIRST_COMPLETED`: Return as soon as **any** task is done.
  - `asyncio.FIRST_EXCEPTION`: Return when **any** task raises an exception.  
    If none raise errors, behaves like `ALL_COMPLETED`.

### Notes
- Tasks in `done` → finished, possibly with result or exception.
- Tasks in `pending` → still running in the background.

```python
done, pending = await asyncio.wait(aws, timeout=5)
```

---

## `asyncio.timeout(delay)`
**`awaitable context manager`**

Returns an `asyncio.Timeout` context manager to limit how long to wait for a coroutine to finish.  
If `delay=None`, no timeout is set (waits forever).

- Automatically cancels the task if it runs longer than the given time.
- cancelling Tasks Raise `CancelledError` catch and converted to `TimeoutError`.

### Parameters
- `delay`: Seconds to wait (`float`, `int`, or `None`).

```python
async def main():
    async with asyncio.timeout(10):
        await long_running_task()
```

---

## `asyncio.timeout_at(when)`
Same as asyncio.timeout(), but instead of a delay, you give it an absolute time
(e.g., loop.time() + 5) to stop waiting.

### Parameters
- `when`: Absolute deadline by loop.time (float or None).

```python
async def main():
    loop = get_running_loop()
    deadline = loop.time() + 20
    async with asyncio.timeout_at(deadline):
        await long_running_task()
```

---

## `asyncio.to_thread(func, /, *args, **kwargs)`
Returns a **coroutine** that will run the given **blocking function** (`func`) in a separate **thread**, preventing the event loop from freezing.

- The `to_thread()` function itself is **not awaitable** — it returns a coroutine which **you must `await`**.
- Passes all `*args` and `**kwargs` to the target `func`.
- Automatically shares the current `contextvars.Context` from the event loop to the new thread.

### Parameters
- `func`: The blocking function to run in a thread.
- `*args`, `**kwargs`: Arguments passed to `func`.

```python
import asyncio, time

def blocking_io():
    print("Start IO:", time.strftime('%X'))
    time.sleep(1)
    print("Done IO:", time.strftime('%X'))

async def main():
    print("Main started:", time.strftime('%X'))
    await asyncio.gather(
        asyncio.to_thread(blocking_io),
        asyncio.sleep(1)
    )
    print("Main done:", time.strftime('%X'))

asyncio.run(main())
```

---

## `asyncio.run_coroutine_threadsafe(coro, loop)`
`thread-safe`  

Used to run asyncio code from **another thread** (e.g., a `threading.Thread`).  
This function **submits a coroutine** to run in a specific event loop from a different OS thread.
> ✅ Thread-safe — safe to call from outside the event loop.

- Returns a `concurrent.futures.Future` object (not an asyncio Future).
- Use .result(timeout) to wait for its result.

### Parameters
- `coro`: The coroutine to run.
- `loop`: The event loop where coro will be scheduled.

### 🧠 Comparison:
|               | `await coro` (inside async)  | `run_coroutine_threadsafe(...).result()` (from thread) |
| ------------- | ---------------------------- | ------------------------------------------------------ |
| Async context | ✅ Required                  | ❌ Not needed (used in threads)                        |
| Blocks thread | ❌ No                        | ✅ Yes (but only your thread, not the loop)            |
| Use case      | Inside `async def` functions | Inside normal `def`, like from `threading.Thread`      |


```python
import asyncio

coro = asyncio.sleep(1, result=3)
future = asyncio.run_coroutine_threadsafe(coro, loop)

result = future.result(timeout=2)
assert result == 3
```

---

## `asyncio.as_completed(aws, *, timeout=None)`
**`asyncio iterator`**

Run multiple awaitables concurrently and get results **as they finish**, not in order.
Returns an **iterator** that yields each completed awaitable one-by-one.

- **`async for`**: yields original tasks (preserves identity).
- **`for`**: yields wrapper coroutines (requires `await` to get result).

### 📥 Parameters
- `aws`: Iterable of awaitables (coroutines, Tasks, or Futures).
- `timeout`: (Optional) Time in seconds to wait for **all** awaitables. Raises `TimeoutError` if exceeded.


### ✅ Example: async for

```python

async def main():
    ipv4 = asyncio.create_task(open_connection("127.0.0.1", 1))
    ipv6 = asyncio.create_task(open_connection("::1", 2))
    tasks = [ipv4, ipv6]

    async for task in as_completed(tasks):
        result = await task
        print(result)
```

---

## `asyncio.eager_task_factory(loop, coro, *, name=None, context=None)`
This factory function makes coroutine objects start executing immediately when a task is created — instead of waiting to be scheduled by the event loop.
- Best used when you want coroutines to **run right away**, but only if they don’t hit `await`.
- Use with: `loop.set_task_factory(asyncio.eager_task_factory)`
- If the coroutine reaches an await, it gets paused and scheduled like normal.
- Mostly helpful in **special environments** or **low-latency async systems**.

### Parameters
- `loop`: The event loop where the task should run.
- `coro`: The coroutine object to run.
- `name`: (optional) Name for the task.
- `context`: (optional) A `contextvars.Context` object to pass a custom scope.

```python
loop.set_task_factory(asyncio.eager_task_factory)
task = asyncio.create_task(my_coroutine())  # Runs immediately if no await
```

---

## `asyncio.create_eager_task_factory(custom_task_constructor)`
Creates a **custom eager task factory** using your own task constructor. This gives you **control over how tasks are created and run**.

- Takes a callable that mimics `Task.__init__()` and returns a Task-compatible object.
- Your constructor must accept an `eager_start` keyword argument.
- Use it like:

```python
loop.set_task_factory(
    asyncio.create_eager_task_factory(my_custom_task_constructor)
)
```
> Most users won’t need this — just use asyncio.eager_task_factory directly.
> for more info read docs

### Parameters
- `custom_task_constructor`: A callable that creates and returns a Task-compatible object. Must support **eager_start**.

```python
# Custom example
def my_constructor(loop, coro, *, name=None, context=None, eager_start=False):
    return asyncio.Task(coro, loop=loop, name=name)

loop.set_task_factory(asyncio.create_eager_task_factory(my_constructor))
```

---

## `asyncio.Runner(*, debug=None, loop_factory=None)`

A **low-level context manager** used to manually create, run, and clean up an event loop. Mostly used when you need more control — like inside **IPython**, **sync apps**, or when writing custom asyncio tools.

- Introduced in **Python 3.11**
- Inherit `builtins.object`
- Good when you want to run async code in a limited scope

> Think of it as: “I just want to use asyncio *here* and clean up after.”

### Parameters
- `debug`: Run the loop in debug mode (optional).
- `loop_factory`: Use a custom event loop (like `uvloop.new_event_loop()`) (optional).

### Methods
| Method                         | Description                                                                                         |
|-------------------------------|-----------------------------------------------------------------------------------------------------|
| `run(coro, *, context=None)`  | Runs a coroutine inside the Runner’s event loop. You can pass a `contextvars.Context` object to control variable scope. |
| `get_loop()`                  | Returns the internal event loop managed by the Runner. Useful if you need to manually schedule tasks or inspect the loop. |
| `close()`                     | Finalizes async generators, shuts down the default executor, and releases any internal resources like context vars.        |

And also includes: `__init__`, `__aenter__`, `__aexit__`, `__dict__`, `__weakref__` (used by Python internally).

```python
with asyncio.Runner() as runner:
    result = runner.run(my_coroutine())
```

---

## `asyncio.Timeout(when: Optional[float])`
**`Low-level async context manager`**

Cancels long-running tasks when they go beyond the deadline (when).
You shouldn’t use this directly — use timeout() or timeout_at() instead.
> If timeout occurs, asyncio.CancelledError is converted to TimeoutError.

### Parameters
- `when`: **Absolute deadline in seconds** (loop.time() + x) or None.

### Methods
| Method             | Description                               |
| ------------------ | ----------------------------------------- |
| `when()`           | Returns the current deadline or `None`.   |
| `reschedule(when)` | Change the timeout deadline.              |
| `expired()`        | Returns `True` if the timeout has passed. |

> Also includes internal methods: `__init__`, `__aenter__`, `__aexit__`, `__repr__`, `__dict__`, `__weakref__`, `__final__`.

```python 
async def main():
    try:
        async with asyncio.Timeout(loop.time() + 10):
            await long_running_task()
    except TimeoutError:
        print("The long operation timed out.")

    print("This will still run.")
```

---

## `asyncio.Task(coro, *, loop=None, name=None, context=None, eager_start=False)`
**`not thread-safe`**

A Future Like object that runs a coroutine inside it concurrently, Wraps a coroutine in a task and schedules it to run in the event loop. Tasks enable multiple coroutines to run concurrently: when one awaits (pauses), the event loop switches to another ready task.

> Should not use directly use `asyncio.create_task()`
> - If a coroutine awaits on a Future, the Task pauses until the Future completes.  
> - `asyncio.Task` inherits from `Future` (but not `set_result()` or `set_exception()`).

### Parameters
- `coro`: The coroutine object to run.
- `loop`: Event loop to run the task on. *(Deprecated — only use if no running loop is active).*
- `name`: Optional task name (used for debugging).
- `context`: A [`contextvars.Context`] to run the task in.
- `eager_start`: If `True`, run immediately until first block (await) or completed. Otherwise, schedules the task in event loop. like normal.

### Methods

| Method                    | Description |
|---------------------------|-------------|
| `cancel(msg=None)`        | Request cancellation. Injects `CancelledError` into coroutine. |
| `cancelled()`             | Returns `True` if task was cancelled. |
| `cancelling()`            | Returns how many times `.cancel()` was called. |
| `uncancel()`              | Decreases cancellation request count. |
| `done()`                  | `True` if the task is finished (result, exception, or cancelled). |
| `exception()`             | Returns exception raised by the task (or raises `InvalidStateError` if not done). |
| `get_context()`           | Returns the context in which the task is running. |
| `get_coro()`              | Returns the coroutine object wrapped by the task. |
| `get_name()`              | Returns the task's name. |
| `get_stack(limit=None)`   | Returns coroutine stack frames (if suspended). else empty list |
| `print_stack(limit=None)` | Prints the stack (like traceback). |
| `result()`                | Returns the task result (or raises if not done or has error). |
| `set_exception(exception)`| Mark the future done and set an exception, if done raises InvalidStateError. |
| `set_result`              | Mark the future done and set its result, if done raises InvalidStateError. |
| `set_name(value)`         | Sets the task name. |
| `add_done_callback(fn,context)`| Calls `fn(task)` when done. |
| `remove_done_callback(fn)`| Removes `fn` from done callbacks. |

> 🔎 Dunder and inherited methods: `__init__`, `__del__`, `__iter__`, `__repr__`, `__await__()`, `__class_getitem__`, `__new__`, and `get_loop()` (from `Future`)

```python
import asyncio

async def say_hello():
    await asyncio.sleep(1)
    print("Hello from task!")

async def main():
    task = asyncio.create_task(say_hello(), name="MyTask")

    print(f"Task started: {task.get_name()}")
    await task
    print("Task done.")

asyncio.run(main())
```

---

## `asyncio.TaskGroup(*, loop=None, name=None)`

An asynchronous context manager holding a group of tasks.
Tasks can be added using `.create_task()`. All tasks are awaited when the context manager exits.

- Inside `async with`, you can still create new tasks (even from within running coroutines).
- Once the `async with` exits (`__aexit__` is called), no new tasks can be added.
- If any task raises an exception:
  - Inside the block: 
    - All tasks are cancelled (except ones already done).
    - The task running the async with block is also cancelled.
    - But you’ll still see the real exception, not just `CancelledError`.
    - at the end all task cancelled and `__aexit__()` called.
  - Outside the block (`__aexit__`): 
    - All other tasks are cancelled (except if the exception is `CancelledError`).
    - and `__aexit__()` called
- All raised exceptions are grouped into `ExceptionGroup` or `BaseExceptionGroup`.
- If the error is `SystemExit` or `KeyboardInterrupt`, it is re-raised as-is (not wrapped in ExceptionGroup).
- Nested task groups process their own exceptions separately and cleanly.

### Parameters
- `loop`: *(Deprecated)* Event loop to run tasks in. Use only when no loop is running.
- `name`: Optional group name (for debugging).

### Methods

| Method                          | Description |
|----------------------------------|-------------|
| `__aenter__()`                  | Enters the async context. |
| `__aexit__(et, exc, tb)`        | Exits the context, waits for all tasks. |
| `create_task(coro, *, name=None, context=None)` | Adds a new task to the group. Like `asyncio.create_task()`. |
> others `__init__`, `__repr__`, `__dict__`, `__weakref__`

```python
import asyncio

async def work(n):
    await asyncio.sleep(n)
    print(f"Task {n} done.")

async def main():
    async with asyncio.TaskGroup() as tg:
        tg.create_task(work(1))
        tg.create_task(work(2))

asyncio.run(main())
```

---