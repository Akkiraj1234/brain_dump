[TOC]


<details>
  <summary>Click to view code</summary>
    <pre><code class="language-python">
def hello():
    print("Hello, world!")
    </code></pre>
</details>

# 📚 Curses Module

**The `curses` library lets us build terminal-based applications at a low level.**  It is the **Python binding** for the C-based **ncurses** library. The goal of this binding is to provide all the functionalities of `ncurses` in a **high-level language like Python** with a simpler and more Pythonic interface.

> **For example, Python merges functions like:** `addstr()`, `mvaddstr()`, and `mvwaddstr()` into a single simplified method: `addstr()`.

- **✅ Available by default**  on `Linux`, `Unix`, `macOS`
- ❌ **Not natively supported on Windows** — you need to install it manually using `pip install windows-curses`

## Windows-curses

Windows doesn't support the `curses` module by default because its console system is built differently from Unix-based systems. Unix-like systems (Linux, macOS, etc.) use **escape sequences**—special codes sent directly to the terminal—to handle things like moving the cursor or changing colors. But Windows doesn't follow this architecture. Instead, it uses **system-level API calls** to perform those same tasks. and friends thats the reason i hate window :)

To solve this, the **`windows-curses`** package was created. It works as a **compatibility layer**, translating what curses wants to do into actions the Windows console understands **by calling the appropriate Windows APIs behind the scenes.**

> 📌 Modern Windows terminals *do* support ANSI escape sequences now, but official support for `curses` hasn’t been fully integrated into `ncurses` yet.  [Source – Microsoft Docs](https://learn.microsoft.com/en-us/windows/console/console-virtual-terminal-sequences?utm_source=chatgpt.com)

> 🧠 Windows provides a rich Console API for writing text, changing colors, moving the cursor, and more — all done through system calls rather than escape codes.  [Source – Microsoft Blog](https://devblogs.microsoft.com/commandline/windows-command-line-inside-the-windows-console/?utm_source=chatgpt.com)

## What is Ncurses

`ncurses` is a powerful C-based library that lets you build advanced, interactive text-based user interfaces (TUIs) inside a terminal. It gives your terminal application the ability to do things like move the cursor, change text colors, draw boxes and windows, and create menus or input fields — all using plain text.

Normally, doing these things would require writing complicated, terminal-specific escape codes, since every terminal behaves a little differently. `ncurses` solves this problem by acting as a universal translator: it looks up how a terminal works using a standardized database (`terminfo` or `termcap`) and translates your simple function calls into the correct low-level codes for that specific terminal.

This makes your application portable — it can run on almost any terminal without needing to worry about compatibility.

> Learn more about the [history of ncurses](#history-of-ncurses).Features

## Key Features

1. Works with almost **all terminals**, so apps made with it run pretty much anywhere.
2. Acts as the **core engine behind terminal UIs** in many languages (C, Python, Rust, etc.).

---

# 🚀 Capabilities of Curses and Ncurses

As you know a terminal is essentially a grid made up of rows and columns, where each "cell" can be uniquely identified by coordinates `(row, col)`,  kind of like a pixel in a graphic interface, but for text. What makes `ncurses` powerful is its ability to control **each individual cell** of that terminal screen.

With `ncurses`, you’re not limited to simply printing lines , you get **full control**. You can customize each cell’s appearance, **take real-time input from the keyboard** or **mouse**, create **pop-up windows**, handle **scrolling regions**, and so much more. It transforms the terminal from a basic output tool into an interactive, dynamic UI playground.

## What You Can Do with Ncurses (in Detail)

- **`Move the Cursor` :** Position the cursor anywhere on the screen. You can even make it invisible or control its visibility.
- **`Draw Text Anywhere` :** Output text at any screen cell, without having to print line-by-line. Design your own custom layout like a UI toolkit.
- **`Style Your Text` :**Make text **standout**, **blink**, appear **dim**, **bold**, *italicized*, or **reversed**. Every cell can be visually customized.
- **`Color Control` :**  Change **foreground** and **background** colors. Combine this with styling like bold, underline, or reverse to make your terminal UI pop.
- **`Mouse Input` :** Capture mouse clicks and movements (if supported by the terminal). Great for menus, selections, or drawing tools.
- **`Keyboard Input` : **Detect keypresses in real time, including special keys like arrows, ESC, and F1–F12. Perfect for building games, file managers, or custom shortcuts.
- **`Window Management` :** Split the terminal into multiple windows, **sub-windows**, or **pop-ups**. Each can function independently and update separately.
- **`Scrollable Regions` :** Create areas that scroll **vertically** or **horizontally**, useful for long content like chat windows, file lists, or logs.
- **`Pad Support` :** Use “pads”,  virtual screens larger than the physical terminal. Scroll through them like you're moving around a giant canvas.
- **`Smooth Updates` :** **Only redraw what’s changed**, reducing flicker and improving performance. This gives your app a slick, modern feel.
- **`Terminal Independence` :** Ncurses handles quirks of different terminals under the hood, so your app works on most systems without changes.

## Bonus Features (Advanced but Super Handy)

- **Screen Snapshots :** Save and restore the terminal’s state, like taking a screenshot. Useful for switching between views or modes.
- **Non-Blocking Input & Timers :** Handle real-time actions, animations, or background tasks without freezing your app.
- **Custom Key Bindings :** Set up your own shortcuts or commands using function keys, Ctrl/Alt combos, and more.

## What Can You Build with Curses?

With the `curses` library, the possibilities are endless. You’re not limited to just building basic applications – you can create immersive, interactive experiences right in the terminal.

- **Real-time input handling** and **dynamic screen updates** allow you to craft engaging **text-based games** where the player can interact with the environment, move the cursor around, and see instant feedback on their actions.

- Thanks to **window management**, you can easily create **multi-pane layouts** for complex applications like **system monitors**, where real-time data like CPU usage or memory consumption can be displayed across separate sections of the screen.

- You can build **interactive menus**, **file explorers**, or even a **chat application** where multiple sections of the terminal update independently. `Curses`'s ability to **smoothly update only changed areas** and **handle mouse input** opens the door to a more intuitive and efficient user experience.

- With **color handling**, **text attributes** (like bold, underline, or blinking), and **scrolling areas**, you can design apps that stand out and are easy to navigate, even for complex datasets or long logs.

In short, `curses` gives you the power to create terminal apps that are not only functional but also user-friendly and visually appealing. You can move the cursor, handle keyboard and mouse input, update the screen efficiently, and manage multiple windows—all in a seamless way.

---

# 🧠 Core Concepts

some of main core consepts of curses that everyone need to know before working with curses library.

## 1. How Curses Enables Cross-Platform Terminal Control

To understand how `curses` achieves cross-platform compatibility, we first need to understand how terminals work.

In any terminal, performing actions like coloring text, moving the cursor, or handling user input requires sending **escape sequences** (also known as **escape codes**) to the terminal. These escape sequences are special character combinations that tell the terminal what action to perform, such as changing text color or moving the cursor to a specific position.

However, different terminal types (like **xterm**, **gnome-terminal**, **macOS Terminal* use different escape sequences. This means that a terminal application designed for one terminal might not work properly on another because the escape codes vary.

<h3>How Curses Solves This Problem !</h3>

The `curses` library addresses this issue by abstracting away the specifics of each terminal’s escape sequences. It ensures that your terminal-based applications will work across various platforms by managing and translating the escape codes automatically.

- **Terminfo Database**: To handle the differences in escape sequences and terminal features, `curses` uses a database called **terminfo**. This database stores information about which features are available on different terminals and what escape codes are used to control those features (like cursor movement or text styling).
- **Initialization**: When you initialize a `curses` application by calling the `initscr()` function, it first checks the **(`TERM`)** environment variable to identify the terminal you're using. This is how `curses` retrieves the terminal's capabilities from the **terminfo** database. It ensures that `curses` knows exactly which escape sequences to use based on the terminal's capabilities.
- **Escape Code Management**: Instead of letting the User handle escape codes, `curses` takes control. It **encodes** the escape sequences in a standardized way, ensuring compatibility across different platforms and terminal types. By doing this, `curses` eliminates the need for developers to worry about the underlying differences between terminals, making it easier to create applications that work cross-platform.

### Why Curses Does Not Support ANSI Escape Codes Directly?

The reason `curses` doesn't support **ANSI escape codes** directly is because **curses likes to take full control over the terminal**. What does that mean?

Well, the way `curses` works is by using **ANSI codes internally** to update the terminal but it keeps track of everything through its **own internal data structures**. If *you* start using raw ANSI escape codes manually, it won’t know what you changed! And that’s the problem, it could lead to glitches or unpredictable behavior.

**To put it simply:**

> *`curses` is like that loyal girlfriend — she stays committed to you, expects the same in return, and doesn’t want you doing shady stuff behind her back.
> So when you sneak in raw ANSI codes, it’s like texting your ex — `curses` won’t be able to trust you anymore and things will fall apart. (0-0)*

Because `curses` uses ANSI under the hood and logs every change in its internal buffer, bypassing that system is like breaking the contract — and it loses track of what’s on the screen.

<h4> So how curses treat all the text we print in our terminal?</h4>

Normally, a terminal interprets ANSI escape codes as a sequence of bytes — for example, `\033[3m` is interpreted as:

```shell
ESC [ 3 m
::This tells the terminal: “Turn on italic mode.”
```

However, inside a `curses` program, text which is preteneted in terminal, it treats differntly like a sequence of characters, like:

```she
['\033', '[', '3', 'm']
```

As a result, the terminal doesn’t interpret it as a command — it just displays those characters as plain text, or worse, your layout may break.

---

## 2. Virtual Screen vs Physical Screen (Double Buffering)  

The `curses` library manages **two types of screens**:

1. **Virtual Screen** – This is a hidden screen in memory. It acts like a *drafting layer* where you prepare all your changes before showing them.
2. **Physical Screen** – This is the actual terminal screen you see.

**Together, this setup is called double buffering**. Instead of drawing directly to the screen (which can cause flickering), you update the virtual screen first. Once all your changes are ready, calling `refresh()` pushes only the modified parts from the virtual screen to the physical screen.

### Why Two Screens?

in short answer. **To avoid flickering and improve performance.**

Let’s say you are updating the screen rapidly — like animating text or moving objects in a game. If you draw directly to the visible screen, each little change will show up instantly. This creates a "blinking" or "flickering" effect because the terminal tries to update everything as fast as it can, and it's not always smooth. By using a virtual screen:

- You **build** the final result in the background.
- Then you use `refresh()` to **push the complete frame** to the visible screen — all at once. This is faster and smoother.

### How does it work under the hood?

Terminals display content in a **grid format** (rows and columns). When `curses` compares the virtual and physical screens, it doesn't check every character one by one. Instead, it relies on an **internal data structure** that tracks changes. This structure allows `curses` to quickly determine:

- **What** changed (e.g., a character or color),
- **Where** it changed (e.g., row 5, column 12).

This is done in **constant time** (O(1)), meaning that `curses` can quickly figure out what needs to be updated without needing to scan the entire screen. Instead of redrawing the whole screen, it updates **only the changed parts**, making the process much faster and more efficient.

---

## 3. Types of Windows in Curses

Curses lets us divide the terminal into multiple *windows* to manage content more efficiently. Think of windows as separate rectangular regions that can be drawn and updated independently. This is super useful for building interfaces like dashboards, forms, or games.

There are **5 main types of windows** you’ll work with in curses. Let’s break them down one by one.

### 1. Standard Screen (`stdscr`)

This is the default window. You don’t even need to create it — it's there the moment you run `initscr()`. **Think of it as the "main canvas"**

- Covers the entire terminal screen.
- Most simple programs just use `stdscr` to draw everything.
- You can think of it as the **"root window"** or **"main canvas"**

### 2. Normal Window (`newwin()`)

Now, if you want to break your screen into smaller sections, this is where `newwin()` comes in.

- You can create multiple independent windows like this.
- Each one has its **own buffer**, meaning what you draw in one won’t affect the others.
- Great for sidebars, footers, status panels, headers, menus, etc.

### 3. Sub-window (`subwin()`)

This is a bit tricky, A `subwin` is a window *inside* another window.

- It **shares the same memory buffer** as the parent window.
- So if you draw on the subwindow, it also affects the parent — and vice versa.
- Useful if you want to divide a window without using extra memory.

> ⚠️ Be careful — since the memory is shared, unexpected things can happen if both are updated at the same time.

### 4. Pad (`newpad()`)

Pads are *like windows* but bigger than the screen, Scrollable behavior is what makes pads special.

- You can create a giant off-screen pad (e.g., 1000 lines).
- Then you control what portion of it is visible on the screen.
- You’ll need to use `prefresh()` instead of `refresh()` to show content from the pad.

> 💡 Use this when your content is too big for the screen. Like chat history, logs, or scrollable terminals.

### 5. Derivative Window (`derwin`)

This one is like `subwin()`, but safer and more flexible.

- Also created from a parent window.
- It **shares the buffer**, like `subwin()`.
- But uses **coordinates relative to the parent**, not the screen.
- That makes it easier to manage complex nested layouts.

### Quick Comparison Table:



| Type       | Independent Window? | Shares Buffer? | Scrollable? | Good For                        |
| ---------- | ------------------- | -------------- | ----------- | ------------------------------- |
| `stdscr`   | Yes                 | No             | No          | Main base window (default)      |
| `newwin()` | Yes                 | No             | No          | Multiple UI sections, isolation |
| `subwin()` | No                  | Yes            | No          | Low-memory sub-sections         |
| `newpad()` | Yes                 | No             | Yes         | Logs, chat history, scrolling   |
| `derwin()` | No                  | Yes            | No          | Clean nested layouts inside UIs |

---

## 4. Curses vs Shell Terminal (How curses *takes over* the terminal)

When you run a **curses** application, you'll notice it **clears everything on your terminal** and starts what looks like a new screen. That’s because curses creates its own window and takes full control of the terminal. Once you quit the app, it **returns you to the original terminal state**, just like how it was before you launched the curses program.

Basically, curses makes a **snapshot** of your terminal — all the text and state — then clears it to draw its own UI. When the program ends, it restores that snapshot so it feels like nothing changed.

- **Shell Terminal** → The normal screen you’re using before the curses app starts
- **Curses Window** → A separate screen created by curses to handle custom layout, rendering, and input

### What actually happens behind the scenes:

- Curses calls `initscr()`, which saves the current state of the terminal (like shell layout, cursor mode, input behavior, etc. )
- It then switches the terminal to **raw mode**, disables line buffering, and hides the cursor — giving curses complete control over how the terminal behaves
- The screen you're seeing is no longer your regular shell — it's a **virtual screen managed entirely by curses**
- During execution, all output, input, and UI updates go through the curses system (not your shell)
- When the program exits (via `endwin()`), curses restores the terminal to its original state — as if it was never there

> This “takeover and restore” mechanism is what allows curses to build UIs without permanently messing with your terminal.

## 5. Keyboard & Mouse Input Handling in `curses`

Curses allows you to handle input directly from the terminal, giving you control over the keypresses and mouse events. This is what happens:

### 🔑 Keypress Events

In curses, every key you press is captured and handled by the program. This means you don’t need to wait for the user to press "Enter" — curses can detect any keypress instantly.

- When a key is pressed, it returns a specific **number** based on the key.  
- Special keys like the arrow keys, function keys, and others are detected using **constants**.

### 🚀 Special Keys & Constants

Curses defines constants for special keys like:

- Arrow keys
- Function keys (F1, F2, etc.)
- Other terminal-specific keys

For example, when you press the up arrow, curses will return a constant value `KEY_UP`. Without enabling **keypad mode**, the program will receive random values instead of these specific constants, making it difficult to detect special keys.

You enable **keypad mode** to ensure that special keys are captured correctly and handled by the program.

### 🖱️ Mouse Support

Curses can even handle mouse events, like detecting mouse clicks and tracking the mouse's position on the terminal screen.

To enable mouse support, you use a special function to activate mouse tracking, which allows curses to capture mouse events like clicks and movements.

Mouse support is available on most Linux and macOS terminals. On Windows, you’ll need to install `windows-curses` or use an emulator that supports it.

---

## 6. Different input & display modes

In terminal-based applications, we often need to control **how input is taken** from the user and **how output is displayed**. `curses` gives us full control over these behaviors using a bunch of modes. These help you fine-tune your app for different situations — like typing a password, building a game, or showing logs with no delay.

Let’s go through the most useful modes, one by one.

### 1. `echo mode` vs `noecho mode`

By default, when a user types something in a terminal, it shows up on the screen. This is called **echo mode**

- `echo()`
   The user's input appears on the screen.
   ✅ Good for: forms, chat apps, general input boxes.

- `noecho()`
   The user's input is **hidden** while typing.
   ✅ Good for: passwords, PIN inputs, anything sensitive.

### 2. `cbreak mode` vs `raw mode`

By default, the terminal waits for the **Enter key** before sending input. This is called **Row mode**

- `cbreak()`
   Sends input **immediately** to your program, character by character — no need to press Enter.
   ✅ Good for: interactive UIs, key listeners.
- `raw()`
   Like `cbreak`, but even more low-level.
   It disables control key handling (e.g. Ctrl+C won't stop the program unless you code it yourself).
   ✅ Good for: games, key-based navigation, full custom control.

### 3.  Keypad Mode

```python
keypad(win, True)
```

Some keys like arrows, function keys, etc., don’t return readable characters — they return strange escape codes.

To make sense of them, enable **keypad mode** on your window (usually on `stdscr`).

### 4. `Nodelay mode` vs `Halfdelay mode`

By default, `getch()` waits forever until the user presses a key. You can make it non-blocking (or semi-blocking) with these:

- `nodelay(True)`
   Makes `getch()` **non-blocking** — it returns `-1` if no key is pressed.
   ✅ Great for: animations, real-time games, background checks.
- `halfdelay(tenths)`
   Like a mini-timeout — waits **a little** before continuing.
   Value is in tenths of a second, so `halfdelay(5)` = 0.5s.
   ✅ Good for: user interaction with fallback (e.g., type within 1 sec or auto-move)

### 5.  Cursor Visibility: `curs_set()`

Control how the **cursor** looks during your program, Hide it for fullscreen UIs or games. Show it when expecting input.

```python
curses.curs_set(0)  # Hide
curses.curs_set(1)  # Normal (visible)
curses.curs_set(2)  # Very visible (some terminals support this)
```

# 🏗️ Structure of a curses App

curses follow the structure of curses app

1. **[Initialize the screen](#️-initialize-the-screen-and-cleanup)**  
2. **[Work with text, Refresh and input](#work-with-text-refresh-and-input)**  
3. **Cleanup** 

### 🛠️ Initialize the Screen and Cleanup

> 📌 **Before doing anything, curses must be initialized using the `initscr()` function.**  
> *It sets up internal data structures based on the terminal type — the way [curses works](#how-curses-works) — and stores the required control codes as constants to use*

1. After `initscr()` is called successfully, it returns a **window object** representing the full terminal screen (rows × columns), which you can use to perform all text-based operations.  
2. This returned window is traditionally named `stdscr`. Using this name helps keep your code familiar and understandable for other developers.  
3. You can manually customize settings either before or after calling `initscr()`. (Read this for advanced or manual setup options.)  
4. Ending a curses session is simple. You usually reverse any settings you changed during setup, and finally restore the terminal to its normal shell mode by calling `curses.endwin()`  
5. To handle setup and cleanup in a clean and professional way, curses provides a helper called `wrapper()`.  
   It manages everything — initialization, error handling, and restoring the terminal — so you can focus just on your application logic.

> 🧾 In short: Start with `initscr()`, end with cleanup — or just let `wrapper()` handle everything.

---

# 📖 Reference & Extras

- 🔗[Python curses wrapper source code](https://github.com/python/cpython/tree/main/Lib/curses)
- 🔗 

- 🔗 [**Official Python Curses HOWTO**](https://docs.python.org/3/howto/curses.html#curses-howto)
   A beginner-friendly guide from the official docs — highly recommended as a starting point.
- 🔗 [**Python `curses` full library reference**](https://docs.python.org/3/library/curses.html)
   Contains all classes, functions, and constants you’ll ever need.
- 🔗 [**`curses.window` methods**](https://docs.python.org/3/library/curses.html#curses.window.get_wch)
   Direct link to the methods of the main window object (`stdscr` and others).
- 🔗 [**Python `curses.panel` module**](https://docs.python.org/3/library/curses.panel.html)
   For managing stacked windows — useful when working with layered UI.
- 🔗 [**Python `curses.textpad` module**](https://docs.python.org/3/library/curses.html#module-curses.textpad)
   Offers ready-made tools for text input and simple editing widgets.
- 🔗 [**Python `curses.ascii` module**](https://docs.python.org/3/library/curses.ascii.html)
   Helps you work with ASCII characters, especially for input filtering.
- 🔗 [**Ncurses C Documentation (man pages)**](https://linux.die.net/man/3/ncurses)
   Low-level, but a treasure for digging deeper or mapping C logic to Python.
- 🔗 [**Ncurses Intro for C Programmers**](https://invisible-island.net/ncurses/ncurses-intro.html)
   Hardcore but amazing if you want to understand the raw terminal magic.

------

### 🧠 Bonus Learning (Optional but Cool)

- 🔗 **Curses programming with Python – Slide deck (external)**
   A visual explanation of `curses` concepts in slide format.
- 🔗 **Real Python: Intro to Curses (unofficial)**
   A clean and practical intro — great for your early-stage notes.
- 🔗 [**Urwid (alternative to curses)**](http://urwid.org/)
   If you ever want to go beyond curses and try a more modern terminal UI lib.
- 🔗 Curses History
