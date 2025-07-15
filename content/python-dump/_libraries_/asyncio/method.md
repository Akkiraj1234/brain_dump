# Asyncio Functions and classes

> **Author** : Akhand Raj  
> **GitHub** : [@Akkiraj1234](https://github.com/Akkiraj1234)  
> **Date**   : 13 July 2025  
> **Status** : ⏳ Ongoing

---

## Topics
1. [function index](#function-index)
2. [Class index](#class-index)
3. [Decreated](#decreated)

---

## function index
| function             | definition                                 |
|----------------------|--------------------------------------------|
| [`asyncio.run(main, *, debug=None, loop_factory=None)` ](#asynciorunmain--debugnone-loop_factorynone) | Create event loop, run a coroutine, close the loop. |
| [`asyncio.create_task(coro, *, name=None, context=None`](#asynciocreate_taskcoro--namenone-contextnone) | Start an asyncio Task, then returns it. |
| [`asyncio.current_task(loop=None)`](#asynciocurrent_taskloopnone) | Return the currently running Task instance, or None if no task is running. |
| [`asyncio.all_tasks(loop=None)`](#asyncioall_tasksloopnone) | Return all tasks that are not yet finished for an event loop. |
| [`asyncio.sleep(delay, result=None)`](#asynciosleepdelay-resultnone) | Sleep for a number of seconds. |
| [`asyncio.gather(*aws, return_exceptions=False)`](#asynciogatheraws-return_exceptionsfalse) | Schedule and wait for things concurrently. | 
| [`asyncio.wait_for(aw, timeout)`](#asynciowait_foraw-timeout) | Run with a timeout. |
| [`asyncio.shield(aw)`](#asyncioshieldaw) | Shield from cancellation. |
| [`async asyncio.wait(aws, *, timeout=None, return_when=asyncio.ALL_COMPLETED)`](#async-asynciowaitaws--timeoutnone-return_whenasyncioall_completed) | Monitor for completion. |
| [] | Run with a timeout. Useful in cases when wait_for is not suitable. |




## Class index
| class                | defincation               | methods         |
|----------------------|---------------------------|-----------------|
| [`asyncio.Runner(*, debug=None, loop_factory=None)`](#asynciorunner-debugnone-loop_factorynone) | A context manager that simplifies multiple async function calls. | `run(coro, *, context=None)`, `get_loop()`, `close()` |
|



## Decreated
| function             | definition                                 |
|----------------------|--------------------------------------------|
|

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
Run awaitable objects in the aws sequence concurrently.

If any awaitable in aws is a coroutine, it is automatically scheduled as a Task.

If all awaitables are completed successfully, the result is an aggregate list of returned values. The order of result values corresponds to the order of awaitables in aws.

If return_exceptions is False (default), the first raised exception is immediately propagated to the task that awaits on gather(). Other awaitables in the aws sequence won’t be cancelled and will continue to run.

If return_exceptions is True, exceptions are treated the same as successful results, and aggregated in the result list.

If gather() is cancelled, all submitted awaitables (that have not completed yet) are also cancelled.

If any Task or Future from the aws sequence is cancelled, it is treated as if it raised CancelledError – the gather() call is not cancelled in this case. This is to prevent the cancellation of one submitted Task/Future to cause other Tasks/Futures to be cancelled.

Return a future aggregating results from the given coroutines/futures.


    Coroutines will be wrapped in a future and scheduled in the event
    loop. They will not necessarily be scheduled in the same order as
    passed in.

    All futures must share the same event loop.  If all the tasks are
    done successfully, the returned future's result is the list of
    results (in the order of the original sequence, not necessarily
    the order of results arrival).  If *return_exceptions* is True,
    exceptions in the tasks are treated the same as successful
    results, and gathered in the result list; otherwise, the first
    raised exception will be immediately propagated to the returned
    future.

    Cancellation: if the outer Future is cancelled, all children (that
    have not completed yet) are also cancelled.  If any child is
    cancelled, this is treated as if it raised CancelledError --
    the outer Future is *not* cancelled in this case.  (This is to
    prevent the cancellation of one child to cause other children to
    be cancelled.)

    If *return_exceptions* is False, cancelling gather() after it
    has been marked done won't cancel any submitted awaitables.
    For instance, gather can be marked done after propagating an
    exception to the caller, therefore, calling ``gather.cancel()``
    after catching an exception (raised by one of the awaitables) from
    gather won't cancel any other awaitables.

## `asyncio.wait_for(aw, timeout)`
**`awaitable`**\
Wait for the aw awaitable to complete with a timeout.

If aw is a coroutine it is automatically scheduled as a Task.

timeout can either be None or a float or int number of seconds to wait for. If timeout is None, block until the future completes.

If a timeout occurs, it cancels the task and raises TimeoutError.

To avoid the task cancellation, wrap it in shield().

The function will wait until the future is actually cancelled, so the total wait time may exceed the timeout. If an exception happens during cancellation, it is propagated.

If the wait is cancelled, the future aw is also cancelled.

Wait for the single Future or coroutine to complete, with timeout.

    Coroutine will be wrapped in Task.

    Returns result of the Future or coroutine.  When a timeout occurs,
    it cancels the task and raises TimeoutError.  To avoid the task
    cancellation, wrap it in shield().

    If the wait is cancelled, the task is also cancelled.

    If the task suppresses the cancellation and returns a value instead,
    that value is returned.

    This function is a coroutine.

## `asyncio.shield(aw)`
**`awaitable`**\
Protect an awaitable object from being cancelled.

If aw is a coroutine it is automatically scheduled as a Task.

The statement:

task = asyncio.create_task(something())
res = await shield(task)
is equivalent to:

res = await something()
except that if the coroutine containing it is cancelled, the Task running in something() is not cancelled. From the point of view of something(), the cancellation did not happen. Although its caller is still cancelled, so the “await” expression still raises a CancelledError.

If something() is cancelled by other means (i.e. from within itself) that would also cancel shield().

If it is desired to completely ignore cancellation (not recommended) the shield() function should be combined with a try/except clause, as follows:

Wait for a future, shielding it from cancellation.

    The statement

        task = asyncio.create_task(something())
        res = await shield(task)

    is exactly equivalent to the statement

        res = await something()

    *except* that if the coroutine containing it is cancelled, the
    task running in something() is not cancelled.  From the POV of
    something(), the cancellation did not happen.  But its caller is
    still cancelled, so the yield-from expression still raises
    CancelledError.  Note: If something() is cancelled by other means
    this will still cancel shield().

    If you want to completely ignore cancellation (not recommended)
    you can combine shield() with a try/except clause, as follows:

        task = asyncio.create_task(something())
        try:
            res = await shield(task)
        except CancelledError:
            res = None

    Save a reference to tasks passed to this function, to avoid
    a task disappearing mid-execution. The event loop only keeps
    weak references to tasks. A task that isn't referenced elsewhere
    may get garbage collected at any time, even before it's

## `async asyncio.wait(aws, *, timeout=None, return_when=asyncio.ALL_COMPLETED)`
**`awaitable`**\
Run Future and Task instances in the aws iterable concurrently and block until the condition specified by return_when.

The aws iterable must not be empty.

Returns two sets of Tasks/Futures: (done, pending).

Usage:

done, pending = await asyncio.wait(aws)
timeout (a float or int), if specified, can be used to control the maximum number of seconds to wait before returning.

Note that this function does not raise TimeoutError. Futures or Tasks that aren’t done when the timeout occurs are simply returned in the second set.

return_when indicates when this function should return. It must be one of the following constants:

Constant

Description

asyncio.FIRST_COMPLETED
The function will return when any future finishes or is cancelled.

asyncio.FIRST_EXCEPTION
The function will return when any future finishes by raising an exception. If no future raises an exception then it is equivalent to ALL_COMPLETED.

asyncio.ALL_COMPLETED
The function will return when all futures finish or are cancelled.























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

And also includes: `__init__`, `__enter__`, `__exit__`, `__dict__`, `__weakref__` (used by Python internally).

```python
with asyncio.Runner() as runner:
    result = runner.run(my_coroutine())
```

## `asyncio.timeout(delay)`

