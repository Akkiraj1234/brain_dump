# Asyncio Programming

> **Author** : Akhand Raj  
> **GitHub** : [@Akkiraj1234](https://github.com/Akkiraj1234)  
> **Date**   : 1 Aug 2025  
> **Status** : Completed

---

`asyncio` is a Python library used to write **concurrent code** using the `async` and `await` keywords. It's built around the concept of an **event loop**, allowing you to run multiple I/O-bound operations *asynchronously* within a single thread.

---

## 📚 How to Study Asyncio?

There are two approaches to learning `asyncio`, depending on your goals:

1. **High-Level** – For writing async applications (✅ we will focus on this)  
2. [**Low-Level**](#️-low-level) – For building async libraries or contributing to the `asyncio` internals (❌ not covered here)
3. [**async programming Intro**](./defination.md) – For learning how to use async tools in real life code how to deal with stuff

> We will only cover **High-Level APIs**, as they are enough to build robust async applications.  
> If you're building low-level frameworks or libraries, check the official docs for Low-Level APIs.  
> ⚠️ *Low-level APIs are not recommended for general async app development.*

---

## 🧭 Topics
1. [**Async Programming Intro**](./defination.md)
2. [**High Level**](./method.md)
3. [**Low Level**](#️-low-level)
4. [**Resources**](#-resources)

---

## ⚙️ [Low-Level](https://docs.python.org/3/library/asyncio.html#module-asyncio)

> You don't need this for normal async apps.  \
> These are useful only if you're building **low-level libraries** or working deep with the **event loop**.  \
> (Think: framework developers or advanced contributors.)


- [**Intro**]():  
  A short intro to low-level stuff — written by me (Akki).
- [**Event Loop**](https://docs.python.org/3/library/asyncio-eventloop.html):  
  This is the heart of asyncio. It runs tasks, callbacks, handles network stuff, subprocesses — everything.  
- [**Futures**](https://docs.python.org/3/library/asyncio-future.html):  
  Futures are like promises — they represent a value that’s coming later. Used to connect old-style async code with `await`.  
- [**Transports and Protocols**](https://docs.python.org/3/library/asyncio-protocol.html):  
  For high-performance stuff (like building your own HTTP server). Uses callback-style instead of async/await.  
- [**Policies**](https://docs.python.org/3/library/asyncio-policy.html):  
  Lets you customize how event loops are created — useful when you're messing with threads or want special behavior.  
- [**Platform Support**](https://docs.python.org/3/library/asyncio-platforms.html):  
  Asyncio works on most systems, but some things (like event loops) behave differently on Windows, Linux, etc.  
- [**Extending asyncio**](https://docs.python.org/3/library/asyncio-extending.html):  
  If you're building your own event loop or deep extension, this helps. You probably won’t need it — but it's there.

## 📁 Resources

- [Official Documentation](https://docs.python.org/3/library/asyncio.html#module-asyncio)
- [Source Code (CPython)](https://github.com/python/cpython/tree/3.13/Lib/asyncio)
- [Official High-Level API Index](https://docs.python.org/3/library/asyncio-api-index.html)
- [Official Low-Level API Index](https://docs.python.org/3/library/asyncio-llapi-index.html)
- [Official Developing with asyncio](https://docs.python.org/3/library/asyncio-dev.html)
- [Future-asyncio](https://docs.python.org/3/library/asyncio-future.html)