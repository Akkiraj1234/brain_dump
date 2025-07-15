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
- 






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



