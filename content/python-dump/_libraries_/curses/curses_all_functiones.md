# Curses Functions & Coding 

This document serves as a practical guide to understanding how Python's curses functions work, helping you identify which function suits which task and when to use them. But before diving in, make sure to read the foundational theory covered in [cursse.md](cursse.md). That doc explains all the essential concepts — like the curses buffer system, virtual vs. physical screens, and how curses actually manages the terminal — so you’re not just memorizing functions but truly understanding how everything works under the hood.

## First of All, Let’s Clear a Few Things

- ✅ `ncurses` is **thread-safe** if it’s built that way.
- ⚠️ Python curses isn’t GIL-safe — if you go multithreaded and touch curses from more than 1 thread
- 📄 as mentioned earlier **Before diving in, read this first**: [cursse.md](cursse.md)

> And if you don’t understand something… well, amm, you can search it 🙂. Stack Overflow exists for a reason — I can’t cover everything, even if I want to 🫠.

## 2. Resources I’m Using (and You Should Too)

> I got tired of Stack Overflow's hide-n-seek and read the actual source code.
>  Yeah, I'm that kinda nerd (0-0)

- 📚 [Python Curses Docs](https://docs.python.org/3/library/curses.html#curses.window.get_wch)
- 🧠 [ncurses Source Code](https://github.com/mirror/ncurses/blob/master/ncurses/base)
- 🐍 [Main Python `curses/__init__.py`](https://github.com/python/cpython/blob/main/Lib/curses/__init__.py)
- 🧠🐍 [CPython `_cursesmodule.c`](https://github.com/python/cpython/blob/main/Modules/_cursesmodule.c)


## 3. What’s the Goal?

I’m gonna cover **every `curses` function** available in Python.
 Also, gonna highlight functions that **exist in `ncurses` but are missing in Python**.

There’ll be **two parts**:

1. A categorized list — short and sweet, easy to browse.
2. A deep-dive section — detailed breakdowns. You can scroll or click from the list above.

> I’m breaking it into categories to make life easier.
>  So yeah — sit tight, buckle up, and enjoy this *cursed* ride 🤘

---

# Tables of content
- [Curses Functions \& Coding](#curses-functions--coding)
  - [First of All, Let’s Clear a Few Things](#first-of-all-lets-clear-a-few-things)
  - [2. Resources I’m Using (and You Should Too)](#2-resources-im-using-and-you-should-too)
  - [3. What’s the Goal?](#3-whats-the-goal)
- [Tables of content](#tables-of-content)
- [Curses Functions Short Notes](#curses-functions-short-notes)
  - [1. Initialization \& Termination Routines](#1-initialization--termination-routines)
  - [2. Input Handling Routines](#2-input-handling-routines)
  - [3. Mouse Handling Routines](#3-mouse-handling-routines)
  - [4. Output \& Screen Update Routines](#4-output--screen-update-routines)
  - [5. Mode \& Behavior Settings](#5-mode--behavior-settings)
  - [6. Color and Appearance Management](#6-color-and-appearance-management)
  - [7. Terminal Capabilities \& Environment](#7-terminal-capabilities--environment)
  - [8. Window Management \& Operations](#8-window-management--operations)

# Curses Functions Short Notes

A complete list of all 146+ Python `curses` functions, neatly organized by category.  Each comes with a short, clear definition and a link to a deeper explanation of how it works under the hood — perfect for quick lookups.



## 1. Initialization & Termination Routines

Functions that set up and tear down the curses environment, including saving/restoring terminal states and initializing low‐level terminal information.

| number | name                                     | description                                                  |
| ------ | ---------------------------------------- | ------------------------------------------------------------ |
| 1.     | `curses.initscr()`                       | Initializes the curses system and returns a window object representing the whole screen. |
| 2.     | `curses.endwin()`                        | Ends curses mode and returns the terminal to its normal operating state. |
| 3.     | `curses.def_prog_mode()`                 | Saves the current terminal mode (program state) so it can be restored later. |
| 4.     | `curses.def_shell_mode()`                | Saves the shell’s mode, allowing the terminal to be reset when leaving curses. |
| 5.     | `curses.reset_prog_mode()`               | Restores the terminal to the saved program mode.             |
| 6.     | `curses.reset_shell_mode()`              | Restores the terminal to the saved shell mode.               |
| 7.     | `curses.savetty()`                       | Saves the current tty (teletype) settings of the terminal.   |
| 8.     | `curses.resetty()`                       | Restores the tty settings saved by savetty().                |
| 9.     | `curses.setupterm(term=None, fd=-1)`     | Initializes low-level terminal settings for the specified terminal type. |
| 10.    | `curses.wrapper(func, /, *args, kwargs)` | A convenience function that initializes curses, runs your function, and then cleans up automatically. |
| 11.    | `curses.isendwin()`                      | Returns whether endwin() has been called (i.e. if curses mode has ended). |
| 12.    | `curses.is_term_resized(nlines, ncols)`  | Checks if the terminal’s size has changed compared to provided dimensions. |
| 13.    | `curses.update_lines_cols()`             | Updates curses’ internal record of the terminal’s dimensions. |


## 2. Input Handling Routines

Functions that manage keyboard input and related buffering, including modes for character processing and push-back of characters.

| number | name                       | description                                                  |
| ------ | -------------------------- | ------------------------------------------------------------ |
| 1.     | `curses.echo()`            | Enables echoing of input characters to the screen.           |
| 2.     | `curses.noecho()`          | Disables the automatic echoing of typed characters.          |
| 3.     | `curses.cbreak()`          | Disables line buffering so characters are available immediately (without waiting for Enter). |
| 4.     | `curses.nocbreak()`        | Restores line buffering (ends cbreak mode).                  |
| 5.     | `curses.raw()`             | Puts the terminal into raw mode so that input is passed through without any preprocessing. |
| 6.     | `curses.noraw()`           | Exits raw mode, restoring normal input processing.           |
| 7.     | `curses.halfdelay(tenths)` | Sets a half-delay mode where getch() waits for a fixed tenths-of-a-second interval before timing out. |
| 8.     | `curses.flushinp()`        | Flushes (clears) any typeahead or unread input in the input buffer. |
| 9.     | `curses.ungetch(ch)`       | Pushes a character back onto the input queue, to be read again by getch(). |
| 10.    | `curses.unget_wch(ch)`     | Pushes a wide character back onto the input stream.          |
| 11.    | `curses.has_key(ch)`       | Checks if the terminal recognizes a specific key code.       |
| 12.    | `curses.keyname(k)`        | Returns a string representation of a given key code.         |
| 13.    | `curses.typeahead(fd)`     | Specifies a file descriptor to check for typeahead (pending input) before blocking for user input. |


## 3. Mouse Handling Routines

Functions dedicated to mouse event processing and configuration.

| number | name                                     | description                                                  |
| ------ | ---------------------------------------- | ------------------------------------------------------------ |
| 1.     | `curses.getmouse()`                      | Retrieves a mouse event (click, release, or movement) from the input queue. |
| 2.     | `curses.mouseinterval(interval)`         | Sets the maximum time (in milliseconds) between press and release events to consider them as a click. |
| 3.     | `curses.mousemask(mousemask)`            | Sets the mouse event mask to specify which mouse events the program is interested in. |
| 4.     | `curses.ungetmouse(id, x, y, z, bstate)` | Pushes a mouse event back into the input queue, allowing it to be re-read later. |


## 4. Output & Screen Update Routines

Functions that control screen output, update the display, and manage output delays.

| number | name                      | description                                                  |
| ------ | ------------------------- | ------------------------------------------------------------ |
| 1.     | `curses.delay_output(ms)` | Inserts a delay in output by waiting a specified number of milliseconds. |
| 2.     | `curses.doupdate()`       | Refreshes the physical screen to match all virtual screen changes (batch update). |
| 3.     | `curses.napms(ms)`        | Pauses execution for a specified number of milliseconds, useful for timing in animations. |
| 4.     | `curses.putp`             | Outputs a terminal capability string (often used with terminfo strings) to the terminal. |
| 5.     | `curses.qiflush([flag])`  | Controls whether to flush queued output when an interrupt occurs (interrupt flush control). |


## 5. Mode & Behavior Settings

Functions that change the terminal’s operational modes and behavior for processing input/output.

| number | name                       | description                                                  |
| ------ | -------------------------- | ------------------------------------------------------------ |
| 1.     | `curses.nl()`              | Enables newline translation; a newline on input is translated to carriage return and linefeed on output. |
| 2.     | `curses.nonl()`            | Disables the newline translation behavior.                   |
| 3.     | `curses.noqiflush()`       | Prevents automatic flushing of output when certain keys (like interrupt) are pressed. |
| 4.     | `curses.meta(flag)`        | Enables or disables 8-bit input mode, allowing use of meta (high-bit) characters. |
| 5.     | `curses.filter()`          | Enables filter mode, which is used by programs that accept only one line of input. |
| 6.     | `curses.killchar()`        | Returns the terminal’s current kill character (used to discard input). |
| 7.     | `curses.erasechar()`       | Returns the terminal’s current erase character (used for backspacing or deletion). |
| 8.     | `curses.getsyx()`          | Gets the current virtual cursor position (y, x) without moving it. |
| 9.     | `curses.setsyx(y, x)`      | Sets the virtual cursor position, affecting where the next output will occur. |
| 10.    | `curses.get_escdelay()`    | Retrieves the current delay (in milliseconds) before an ESC key is recognized as a standalone key. |
| 11.    | `curses.set_escdelay(ms)`  | Sets the delay before an ESC key is interpreted as a distinct key press. |
| 12.    | `curses.get_tabsize()`     | Returns the current tab spacing (number of spaces a tab represents). |
| 11.    | `curses.set_tabsize(size)` | Sets the tab spacing to a specified size.                    |
| 12.    | `curses.unctrl(ch)`        | Returns a printable representation of control characters (e.g., converting Ctrl characters to caret notation). |


## 6. Color and Appearance Management

Functions that manage colors, color pairs, and visual attributes for text display.

| number | name                                       | description                                                  |
| ------ | ------------------------------------------ | ------------------------------------------------------------ |
| 1.     | `curses.can_change_color()`                | Checks if the terminal supports redefining its color definitions. |
| 2.     | `curses.color_content(color_number)`       | Returns the red, green, and blue intensities (RGB) of a given color number. |
| 3.     | `curses.color_pair(pair_number)`           | Returns an attribute value representing the specified color pair for use in output. |
| 4.     | `curses.has_colors()`                      | Determines if the terminal supports color display.           |
| 5.     | `curses.has_extended_color_support()`      | Checks whether the terminal supports an extended range of colors beyond the basic set. |
| 6.     | `curses.init_color(color_number, r, g, b)` | Redefines a color’s RGB components for terminals that allow color changes. |
| 7.     | `curses.init_pair(pair_number, fg, bg)`    | Initializes a color pair with a foreground and background color. |
| 8.     | `curses.pair_content(pair_number)`         | Returns the foreground and background colors associated with a given pair number. |
| 9.     | `curses.pair_number(attr)`                 | Extracts the color pair number from an attribute value.      |
| 10.    | `curses.start_color()`                     | Initializes the color functionality within curses.           |
| 11.    | `curses.use_default_colors()`              | Allows the program to use the terminal’s default background and foreground colors. |

## 7. Terminal Capabilities & Environment

Functions that query and manipulate low-level terminal characteristics and capabilities.

| number | name                        | description                                                  |
| ------ | --------------------------- | ------------------------------------------------------------ |
| 1.     | `curses.baudrate()`         | Returns the current baud rate (speed) of the terminal connection. |
| 2.     | `curses.longname()`         | Provides a detailed name or description of the terminal type. |
| 3.     | `curses.termattrs()`        | Returns a set of attributes (like bold, underline) that the terminal supports. |
| 4.     | `curses.termname()`         | Returns the terminal type name as defined by the terminfo database. |
| 5.     | `curses.tigetflag(capname)` | Retrieves a boolean (flag) capability from the terminfo database for the terminal. |
| 6.     | `curses.tigetnum(capname)`  | Retrieves a numeric capability (e.g., number of colors) from terminfo. |
| 7.     | `curses.tigetstr(capname)`  | Retrieves a string capability from terminfo (such as cursor movement sequences). |
| 8.     | `curses.tparm(str[, ...])`  | Processes a parameterized terminal string by substituting given values into its placeholders. |
| 9.     | `curses.use_env(flag)`      | Controls whether curses should respect the LINES and COLUMNS environment variables when setting terminal dimensions. |

## 8. Window Management & Operations

Methods (typically called on window objects) that create, modify, and manage windows and their contents.

| number | name                                              | description                                                  |
| ------ | ------------------------------------------------- | ------------------------------------------------------------ |
| 1.     | `window.addch(y, x, ch[, attr])`                  | Adds a single character (with optional attributes) at the specified position in the window. |
| 2.     | `window.addnstr(y, x, str, n[, attr])`            | Adds at most n characters of a string at the given position with optional attributes. |
| 3.     | `window.addstr(y, x, str[, attr])`                | Adds a string to the window at the specified coordinates with optional attributes. |
| 4.     | `window.attroff(attr)`                            | Turns off a specified text attribute for subsequent window output. |
| 5.     | `window.attron(attr)`                             | Turns on a specified text attribute for subsequent window output. |
| 6.     | `window.attrset(attr)`                            | Sets the window’s current attributes to the specified value. |
| 7.     | `window.bkgd(ch[, attr])`                         | Sets the background property (character and attributes) for the window. |
| 8.     | `window.border([ls, rs, ts, bs, tl, tr, bl, br])` | Draws a border around the window using the specified characters for each side and corner. |
| 9.     | `window.box([vertch, horch])`                     | Draws a simple box around the window using the given vertical and horizontal characters. |
| 10.    | `window.clear()`                                  | Clears all content from the window (but does not refresh the display immediately). |
| 11.    | `window.clrtobot()`                               | Clears the window from the current cursor position to the bottom. |
| 12.    | `window.clrtoeol()`                               | Clears the window from the current cursor position to the end of the line. |
| 13.    | `window.delch([y, x])`                            | Deletes a character from the window at the specified (or current) position. |
| 14.    | `window.deleteln()`                               | Deletes an entire line from the window, scrolling subsequent lines up. |
| 15.    | `window.getch([y, x])`                            | Reads a character from the window at the given position (or current cursor position if omitted). |
| 16.    | `window.getkey([y, x])`                           | Retrieves a key press as a string representation.            |
| 17.    | `window.getmaxyx()`                               | Returns the maximum dimensions (height and width) of the window. |
| 18.    | `window.getyx()`                                  | Returns the current cursor position (y, x) within the window. |
| 19.    | `window.hline(y, x, ch, n)`                       | Draws a horizontal line starting at (y, x) with character `ch` for `n` positions. |
| 20.    | `window.vline(y, x, ch, n[, attr])`               | Draws a vertical line starting at (y, x) using the specified character and attributes for `n` positions. |
| 21.    | `window.move(new_y, new_x)`                       | Moves the window’s cursor to the specified coordinates.      |
| 22.    | `window.refresh()`                                | Updates the physical screen to match the window’s virtual screen content. |
| 23.    | `window.scroll([lines=1])`                        | Scrolls the window content upward by a specified number of lines. |
| 24.    | `window.timeout(delay)`                           | Sets a delay (in milliseconds) for how long `getch()` will wait for input. |
| 25.    | `window.untouchwin()`                             | Resets the modified status of the window (untouches it).     |
| 26.    | `window.bkgdset(ch[, attr])`                      | Sets the background used for clearing the window without immediately redrawing it. |
| 27.    | `window.chgat(y, x, num, attr)`                   | Changes the attributes of a sequence of characters starting at the given position. |
| 28.    | `window.clearok(flag)`                            | Controls whether a window is completely cleared on the next refresh. |
| 29.    | `window.cursyncup()`                              | Synchronizes the physical cursor with the virtual cursor positions in parent windows. |
| 30.    | `window.derwin(nlines, ncols, begin_y, begin_x)`  | Creates a derived (sub)window relative to the current window. |
| 31.    | `window.echochar(ch[, attr])`                     | Displays a character immediately, useful for immediate feedback (echoing) in a window. |
| 32.    | `window.enclose(y, x)`                            | Checks whether the given coordinates fall inside the window’s boundaries. |
| 33.    | `window.encoding`                                 | Holds the encoding used by the window for translating characters. |
| 34.    | `window.erase()`                                  | Erases all content from the window (similar to clear, but may differ in implementation). |
| 35.    | `window.getbegyx()`                               | Returns the (y, x) coordinates of the upper-left corner of the window. |
| 36.    | `window.getbkgd()`                                | Returns the current background property (character and attributes) of the window. |
| 37.    | `window.getstr(y, x, n)`                          | Reads a string of at most n characters starting at the specified position. |
| 38.    | `window.idcok(flag`                               | Control hardware insert/delete line optimizations, immediate update modes, or retrieve a character from a position. |
| 39.    | `window.insch(y, x, ch[, attr])`                  | Inserts a character (with optional attributes) at the specified position in the window. |
| 40.    | `window.insdelln(nlines) / window.insertln()`     | Inserts or deletes whole lines in the window, shifting existing content. |
| 41.    | `window.insnstr(y, x, str, n[, attr])`            | Inserts at most n characters of a string at a specified position. |
| 42.    | `window.insstr(y, x, str[, attr])`                | Inserts a string into the window at the given coordinates.   |
| 43.    | `window.instr(y, x[, n])`                         | Retrieves a string of characters from the window starting at (y, x) for up to n characters. |
| 44.    | `window.is_linetouched(line)`                     | Checks if the specified line has been modified (touched) since the last refresh. |
| 45.    | `window.is_wintouched()`                          | Checks whether any part of the window has been modified.     |
| 46.    | `window.keypad(flag)`                             | Enables or disables keypad mode, which allows the program to capture function keys and special keys. |
| 47.    | `window.leaveok(flag)`                            | Controls whether the cursor should be left where it is after a refresh. |
| 48.    | `window.move(new_y, new_x)`                       | Moves the window’s cursor to the specified coordinates.      |
| 49.    | `window.mvderwin(y, x)`                           | Moves a derived window relative to its parent window.        |
| 50.    | `window.mvwin(new_y, new_x)`                      | Moves the entire window to new absolute screen coordinates.  |
| 51.    | `window.nodelay(flag)`                            | Sets the window’s getch() method to be non-blocking if flag is True. |
| 52.    | `window.notimeout(flag)`                          | Controls whether the window should wait for a key press before timing out. |
| 53.    | `window.noutrefresh()`                            | Marks the window to be updated on the next doupdate() call without immediately refreshing it. |
| 54.    | `window.overlay(destwin, ...)`                    | Overlays the contents of the current window onto another window, preserving blank areas. |
| 55.    | `window.overwrite(destwin, ...)`                  | Overwrites another window with the content of the current window, including blanks. |
| 56.    | `window.putwin(file)`                             | Writes a window’s state to a file, allowing it to be restored later. |
| 57.    | `window.redrawln(beg, num)`                       | Forces a redraw of a range of lines within the window.       |
| 58.    | `window.redrawwin()`                              | Marks the entire window as modified, so it will be completely refreshed on the next update. |
| 59.    | `window.resize(nlines, ncols)`                    | Resizes the window to the specified dimensions.              |
| 60.    | `window.scrollok(flag)`                           | Enables or disables scrolling for the window.                |
| 61.    | `window.setscrreg(top, bottom)`                   | Sets a scrolling region within the window between the specified top and bottom lines. |
| 62.    | `window.standend()`                               | Ends the “standout” (highlighted) mode for the window.       |
| 63.    | `window.standout()`                               | Starts the “standout” mode, often used for emphasis or highlighting text. |
| 64.    | `window.subpad(nlines, ncols, begin_y, begin_x)`  | Creates a new pad (scrollable off-screen window) relative to the current window. |
| 65.    | `window.subwin(nlines, ncols, begin_y, begin_x)`  | Creates a subwindow within the current window with the specified dimensions and position. |
| 66.    | `window.syncdown()`                               | Propagates changes from a parent window down to its subwindows. |
| 67.    | `window.syncok(flag)`                             | Controls whether updates to a window automatically update its ancestors and descendants. |
| 68.    | `window.syncup()`                                 | Forces synchronization of changes from a subwindow to its parent window. |
| 69.    | `window.touchline(start, count[, changed])`       | Marks a range of lines as modified so that they will be refreshed on the next update. |
| 70.    | `window.touchwin()`                               | Marks the entire window as modified, forcing a full refresh. |


