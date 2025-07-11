# 💡facts

1. *yeah in curses we first put the lenght and then  coords from where to start.. its happening since years so no point of changing it now..*
2. **For UI components like buttons and checkboxes, consider learning **Urwid** or **Blessed** for more advanced features.**
3. **You can create smooth animations and interactive apps using curses with timers and non-blocking input.*

# 🖥️ Python Curses Full Syllabus

## 💡 Introduction
- [x] **What is the Python curses module?**
- [x] **What is ncurses?**
- [x] **History of ncurses**
  - [x] Python's support for ncurses
- [x] **Capabilities of curses and ncurses**
  - [x] What can you build with curses?

## 🧠 Core Concepts
- [x] **How curses enables cross-platform terminal control**
- [x] **Virtual screen vs Physical screen**
  - [x] Concept of buffering and double buffering
- [x] **Types of windows in curses:**
  - [x] Standard screen (stdscr)
  - [x] Normal windows (newwin)
  - [x] Sub-windows (subwin)
  - [x] Pads (newpad)
  - [x] Derivative windows (derwin)
- [x] **Curses vs Shell Terminal (How curses "takes over" the terminal)**
- [ ] **Keyboard & Mouse Input Handling**
  - [ ] Keypress events
  - [ ] Special keys & constants
  - [ ] Mouse support
- [x] **Different input & display modes:**
  - [x] Echo / Noecho
  - [x] Cbreak / Raw
  - [x] Keypad mode
  - [x] Nodelay / Halfdelay
  - [x] Cursor visibility

## 🏗️ Structure of a curses App
- [ ] **Initialization and teardown**
  - [ ] `initscr()` vs `wrapper()`
  - [ ] `endwin()`
- [ ] **Main loop structure**
  - [ ] Drawing text
  - [ ] Refreshing windows
  - [ ] Handling user input
  - [ ] Updating logic and UI
  - [ ] Cleanup and restoring terminal

## 🧰 Windows in Detail
- [x] **Creating windows with `newwin()`**
- [x] **Sub-windows vs Derwin**
- [x] **Pads and scrolling content**
- [x] **Box drawing and borders**
  - [x] Managing overlapping windows

## 🎨 Advanced Topics
- [ ] **Colors and color pairs**
- [ ] **Custom text attributes (bold, underline, reverse)**
- [ ] **Animation basics**
- [ ] **Multi-window applications**
  - [ ] Resizing & dynamic layout handling
- [ ] **Debugging a curses app**
- [ ] multitheriding and other in curses
- [ ] **Handling exceptions inside curses safely**

## 🪄 Tips & Tricks
- [x] **Performance tips**
- [x] **Debugging a curses app**
- [x] **Handling exceptions inside curses safely**
  - [x] Keybinding best practices

## 📖 Reference & Extras
- [x] **Complete overview of commonly used curses functions**
- [x] `curses.ascii` module
- [x] **Links to example projects and GitHub repos**
- [x] **Must-read man pages** (`man ncurses`, `man terminfo`, etc.)

# 📦 Additional Curses‑Related Modules

- [ ] **[curses.panel](https://docs.python.org/3/library/curses.html#module-curses.panel)** – Allows stacking windows (panels) with automatic overlap handling via `new_panel()`, `update_panels()`, and `panel()`. Without this, overlapping windows are tricky to manage.

- [ ] **[curses.textpad](https://docs.python.org/3/library/curses.html#module-curses.textpad)** – Provides a Textbox widget and `rectangle()` helper for line‑based editing inside a window. Essential for building simple text editors.

- [ ] **[curses.ascii](https://docs.python.org/3/library/curses.html#module-curses.ascii)** – Utilities for ASCII character classification and control codes (e.g. `isctrl()`, `ord()`, `unctrl()`) useful when sanitizing or mapping input.

---

## 🔍 Low‑Level Terminfo/Termcap APIs

- [ ] **[curses.setupterm(), tigetstr(), tparm()](https://docs.python.org/3/library/curses.html#curses.setupterm)** – Direct access to the terminfo database for custom control sequences (beyond the high‑level wrappers). Useful if you need capabilities not exposed by curses directly.

- [ ] **[curses.putp()](https://docs.python.org/3/library/curses.html#curses.putp)** – Outputs a control string returned by `tigetstr()` to the terminal, bypassing window buffering for special effects.

---

## 🛠 Terminal Mode & Miscellaneous Functions

- [ ] **Saving/restoring terminal modes:**
    - **[curses.def_prog_mode() / curses.reset_prog_mode()](https://docs.python.org/3/library/curses.html#curses.def_prog_mode)** – Let you snapshot the terminal state and restore it, which is crucial when you need to drop into the shell or suspend/resume your app.
    
    - **[curses.def_shell_mode() / curses.reset_shell_mode()](https://docs.python.org/3/library/curses.html#curses.def_shell_mode)** – Let you snapshot the terminal state and restore it when interacting with the shell.
    
- [ ] **[curses.flushinp()](https://docs.python.org/3/library/curses.html#curses.flushinp)** – Clears any pending input.

- [ ] **[curses.delay_output(ms)](https://docs.python.org/3/library/curses.html#curses.delay_output)** – Throttles output to avoid overwhelming slow terminals.

- [ ] **[curses.beep() / curses.flash()](https://docs.python.org/3/library/curses.html#curses.beep)** – For user notifications like a sound beep or screen flash.

- [ ] **[curses.curs_set(0|1|2)](https://docs.python.org/3/library/curses.html#curses.curs_set)** – To hide, show, or make the cursor very visible.

- [ ] **[curses.has_ic() and curses.has_il()](https://docs.python.org/3/library/curses.html#curses.has_ic)** – Detect if the terminal can insert/delete characters/lines.

---

## 📶 Signal Handling & Resize Support

- [ ] **[curses.is_term_resized(nlines, ncols)](https://docs.python.org/3/library/curses.html#curses.is_term_resized)** – Detects window resize. Use it to redraw your UI when the user resizes the terminal.

- [ ] **[curses.resizeterm(nlines, ncols)](https://docs.python.org/3/library/curses.html#curses.resizeterm)** – Changes the terminal size programmatically.

- [ ] **[curses.mouseinterval(ms)](https://docs.python.org/3/library/curses.html#curses.mouseinterval)** – Adjusts click detection delays.

- [ ] **[curses.mousemask()](https://docs.python.org/3/library/curses.html#curses.mousemask)** – Enables/disables mouse event reporting.

---