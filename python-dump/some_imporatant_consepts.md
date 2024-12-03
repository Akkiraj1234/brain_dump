# Important Concepts
Before diving into these topics..

1. [package_managers](./package_manager.md)
2. [environment](./enviorment_and_tools.md)
3. [build-tools](./build_tools.md)
4. deployment
    - [PyPI deployment](./packaging.md)
    - [Executable deployment](./application_dev.md)
    - [Web server deployment](./web_server_deployment.md)
5. **[go back](./_content_.md)**

it is essential to understand the following foundational concepts:

## content
[**package manager**](#package-manager)
 - [pip and pypi](#pip-and-pypi)
 - [System's site-packages Directory](#systems-site-packages-directory)
 - [Module](#module)
 - [libraries](#libraries)
 - [dependencies](#dependencies)
 - [Package](#package)
 - [Dependency Hell](#dependency-hell)
 - [Requirements File](#requirements-file)
 - [Understanding Semantic Versioning](#understanding-semantic-versioning)
 - [NOTES](#notes)
 - [connections](#connections)

[**build-tools**](#build-tools)
 - [wheel and stdist](#wheel-and-stdist)

[**future content**](#future-content)

## **package manager**
A package manager is a tool that simplifies the process of installing, upgrading, configuring, and managing software libraries or dependencies. It automates much of the complexity involved in handling software packages.
- A package manager acts like a tool organizer, ensuring you borrow the correct version of the tool and keep it up-to-date.

### pip and pypi
- **pip (Pip Installs Packages)**: It is the default package manager for Python, allowing you to install, upgrade, and uninstall Python libraries and dependencies from repositories.
- **PyPI (Python Package Index)**: is the official repository for third-party Python packages. Developers publish their libraries on PyPI, making them accessible to others.
- **Test-pypi**: A separate instance of pypi designed for testing and experimenting with package uploads.

### System's site-packages Directory
The site-packages directory is a designated folder within your Python installation where third-party libraries and dependencies are installed.
- For system-wide installations, it’s usually found in directories like /usr/local/lib/python3.x/site-packages (Linux/Mac) or C:\Python3x\Lib\site-packages (Windows).
- For virtual environments, it is specific to the environment and isolated from the system-wide installation.

### Module
A module is a single file containing Python code. It can define functions, classes, and variables, and it may include runnable code. 
- Any Python file (.py) is a module whom we can reuse after import.

### libraries
Libraries, also referred to as packages, are collections of pre-written code that you can use to streamline development. They can be installed via tools like pip and are stored in your system's site-packages directory. Libraries can either be:
- External: Installed from repositories like PyPI.
- Custom: Code you write and reuse across multiple projects.

### dependencies
Dependencies are external libraries or packages that your project relies on but did not create. They are installed from global repositories (e.g., PyPI) and play a critical role in your project's functionality. Your project's success is dependent on these libraries being available and properly configured.

### Package 
A package is a collection of related Python modules organized in a directory structure. It often contains an __init__.py file, which marks the directory as a Python package and can include metadata, settings, or initialization code. A package can include multiple libraries and sub-packages.
-  All libraries can be considered packages if they are bundled as distributable modules. However, not all packages are libraries. Packages can include additional resources (e.g., data files, assets) and sub-packages.

### Dependency Hell
Dependency Hell occurs when conflicting versions of dependencies make it impossible to install or run your project.
#### Causes:
- Two libraries requiring different versions of the same dependency.
- Upgrading one dependency causes a cascade of failures.
#### Solutions:
1. **Isolate Environments:**
   - Use virtual environments to keep project dependencies isolated.
2. **Pin Dependency Versions:**
   - Always specify exact or minimum versions in your `requirements.txt`.
3. **Use Dependency Tools:**
   - Tools like *pipdeptree* or *poetry* can help resolve conflicts and visualize dependencies.

### Requirements File
A requirements.txt file is used to declare your project's dependencies and their versions.
1. **Pin Versions**: Specify exact versions to ensure consistency:
  ```plaintext
  numpy==1.23.0  
  requests>=2.25.0  
  ```
2. **Generate Requirements**: Use `pip freeze > requirements.txt` to create a snapshot of current dependencies.
3. **Handle Sub-Dependencies**: Use **pip-tools** to manage dependency trees and lock files.

### Understanding Semantic Versioning
Semantic Versioning is a versioning system that uses a three-part version number: `MAJOR`.`MINOR`.`PATCH`.
- **MAJOR**: Incremented when you make incompatible API changes.
- **MINOR**: Incremented when you add functionality in a backward-compatible manner.
- **PATCH**: Incremented for backward-compatible bug fixes.

#### Usage in Python
- Specify version constraints using operators:
  - `>=1.0`: Any version greater than or equal to 1.0.
  - `<2.0`: Any version less than 2.0.
  - `~1.0`: Compatible with version 1.0 (e.g., 1.0.1, 1.0.9).
  - `^1.0`: Allow changes that do not modify the first non-zero digit (e.g., 1.x.x).
use under requirment.txt for downloading right package.

### NOTES
- A library can be called a dependency, but not all dependencies can be called libraries.
- If a library is imported into your package, it becomes a dependency. This means that for your project to execute on other platforms or devices, these libraries must be available. Otherwise, the program will fail.
- On the other hand, if the libraries are already present in the package, they are not considered dependencies because they are bundled and readily available in the package.

### connections 
- **donloading :** 
  - `pypi` -> `pip` -> `System's site-packages Directory` -> `Package`
  - Packages are fetched from PyPI using pip, installed into the system's site-packages directory, and organized as Python packages
- **development :** 
  - `Module` -> `libraries` -> `dependencies` -> `Package`
  - Modules combine to create libraries; libraries form dependencies, which are bundled into packages for broader use.

Managing these kinds of things is handled by a package manager.

## **build tools**
Build tools streamline the packaging, distribution, and management of Python projects.

### wheel and stdist
Python supports two types of package distributions:
1. Wheel (`.whl`)
   - A binary distribution format for Python packages.
   - Faster installations because the code is precompiled.
   - Platform-dependent (e.g., Windows, Linux).
   - Created using `python setup.py bdist_wheel`.
2. Source Distribution (`sdist`)
   - A source code archive (e.g., `.tar.gz`).
   - Requires compilation during installation.
   - Platform-independent but slower to install.
   - Created using `python setup.py sdist`.
### Why use wheels? 
- Wheels improve installation speed and minimize platform-related errors.

## future content
1. new topic venv
1. distribution
2. poetry
3. pyproject.toml
4. setup.py
5. setup.cfg
6. setuptools
7. MANIFEST.in
8. Versioning
