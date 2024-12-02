**[`back`](../README.md)**

## python menu level - intermediate
1. [Beginner Level](./beginner.md)
2. [simple consept and defination](./consept_and_defination.md)
3. [Data Types](./data_types.md)
4. [keywords](./keywords.md)
5. [operators](./operators.md)
6. [Build in function](./build-in-function.md)
7. [dunder methods](./dunder_methods.md)
8. [comerhension and teronary](./comerhension.md)
9. [decorators](./decorators.md)
10. [iterators and genrators](./iterators.md)
11. [oops, modules](./oops.md)
12. [Metaclasses](./metaclass.md)
13. [mro detail, interface in python, mixins]()
14. [Memory Management, `__slots__`](./memory_managemnt.md)
    

## python menu - advanced and master
1. [some_important_consepts](./some_imporatant_consepts.md)
2. [package_managers](./package_manager.md)
3. [build tools](./build_tools.md)
4. [poetry_and_other_package_manegers](./poetry.md)
5. [PyPI deployment](./packaging.md)
6. [Executable deployment](./application_dev.md)
7. [Web server deployment](./web_server_deployment.md)
8.  [Concurrency](./concurancy.md) and [library](#concurrency-and-parallelism)
9.  [testing](./testing.md) and [library](#testing-and-quality-assurance)
10. lean framwork: django, flask, aiohttp, tornado, pyramid, [library](#web-development) and [networking](#networking-and-asynchronous-programming)
11. [database](database.md) and [library](#database-interaction)
12. [data_visulization](some.md) and [library](#data-science)
13. [gui](some.md) and [pyqt and tkinter library](#graphical-user-interfaces-guis)
14. [Cryptography and Security](some.md) and [library](#cryptography-and-security)
15. [ctype](ctype.md): for using c++ code in python
16. **cython**: study source code for better understanding

## python new verstion
1. python 3.10
2. python 3.11
3. python 3.12
4. python 3.13



# Python Libraries and Tools

## Core Python Libraries (Essentials)
- **`itertools`**: Tools for efficient looping, such as permutations and combinations.
- **`json` or `pickle`**: 
  - **json**: Parse and generate JSON data.
  - **pickle**: Serialize and deserialize Python objects.
- **`os`, `sys`, `pathlib`**: For file and directory operations (**os**, **pathlib**) and system-specific parameters (**sys**).
- **`time`, `datetime`**: 
  - **time**: Work with timestamps.
  - **datetime**: Manipulate dates and times.
- **`random`**: Generate random numbers and make random choices.
- **`collections`**: High-performance container datatypes like **Counter**, **deque**, and **defaultdict**.
- **`functools`**: Tools for higher-order functions (e.g., **lru_cache**, **partial**).
- **`logging`**: For logging messages across modules.
- **`argparse` or `click`** *(choose one)*:
  - **argparse**: Create command-line interfaces.
  - **click**: Simplified command-line interface creation.
- **`rich`** *(optional)*: For pretty-printing, markdown rendering, and logging in terminals.
- **`shutil`** *(optional)*: High-level file operations like copying and moving files.
- **`subprocess`** *(optional)*: Run external processes and commands.

## Graphical User Interfaces (GUIs)
- **`Tkinter`**: Built-in library for basic desktop GUI applications.
- **`PyQt` or `PySide`**: Feature-rich libraries for building advanced GUIs.
- **`streamlit`** **(optional)**: For creating browser-based apps for data visualization or dashboards.
- **`pygame`** **(optional)**: For 2D game development.
- **`pyopengl`** **(optional)**: Interface to OpenGL for rendering 3D graphics.

## Testing and Quality Assurance
- **`unittest`**: Built-in framework for unit testing.
- **`pytest`**: Advanced testing framework with plugins.
- **`mock`** **(optional)**: Mock objects and test interactions.


## Cryptography and Security
- **`cryptography`**: Robust encryption, decryption, and hashing.
- **`hashlib`**: Hashing algorithms like SHA and MD5.
- **`secrets`**: Generate secure random numbers and tokens.

## Data Science
- **`Pandas`**: Data manipulation and analysis library.
- **`NumPy`**: High-performance numerical computing.
- **`Seaborn`**, **`Matplotlib`** **(optional)**: Statistical data visualization built on top of Matplotlib.

## Concurrency and Parallelism
- **`threading`**: Run threads for multitasking.
- **`multiprocessing`**: Run processes for parallel computing.
- **`concurrent.futures`**: High-level concurrency for threads and processes.

## Web Development
- **`Flask`**: Lightweight framework for building web applications.
- **`Django`**: Full-stack web development framework.
- **`Requests`**: Simplify HTTP requests (GET, POST, etc.).
- **`FastAPI`** **(optional)**: High-performance API creation using Python's `asyncio`.
- **`aiohttp`**, **asyncpy** **(optional)**: For asynchronous HTTP requests.

## Networking and Asynchronous Programming
- **`asyncio`**: For asynchronous programming (e.g., coroutines, event loops).
- **`socket`**: Work with low-level network sockets.
- **`websockets`** **(optional)**: Handle WebSocket connections.
- **`BeautifulSoup`** **(optional)**: Parse and scrape HTML/XML documents.
- **`Scrapy`** **(optional)**: Framework for advanced web scraping.

---

## Database Interaction
- **`SQLite3`**: Built-in library for working with SQLite databases.
- **`csv`**, **`json`**, **`yaml`**: Work with different data serialization formats.
- **`SQLAlchemy`** *(optional)*: Object-relational mapper (ORM) for database interaction.
- **`Django ORM`** *(optional)*: ORM used within Django.
- **`PyMongo`** *(optional)*: Interface for MongoDB.

---

## Miscellaneous Libraries
- **`re`**: Regular expression operations.
- **`platform`** *(optional)*: Retrieve system and hardware information.
- **`cProfile`** *(optional)*: Profile and optimize Python code.
- **`Pillow`** *(optional)*: Image processing and manipulation.
- **`OpenCV`** *(optional)*: Computer vision and image processing.
- **`ConfigParser`** *(optional)*: Work with configuration files.
- **`Numba`** *(optional)*: Speed up Python code using JIT compilation.
- **`Docker`** *(optional)*: Manage and deploy containerized applications.

---

## Notes:
- Items marked as **(optional)** can be skipped if not needed for your use case.
- Advanced sections are focused on specialized topics and projects.
