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
- [Important Concepts](#important-concepts)
  - [content](#content)
  - [**package manager**](#package-manager)
    - [pip and pypi](#pip-and-pypi)
    - [System's site-packages Directory](#systems-site-packages-directory)
    - [Module](#module)
    - [libraries](#libraries)
    - [dependencies](#dependencies)
    - [Package](#package)
    - [NOTES](#notes)
    - [connections](#connections)


## **package manager**
A package manager is a tool that simplifies the process of installing, upgrading, configuring, and managing software libraries or dependencies. It automates much of the complexity involved in handling software packages.
- A package manager acts like a tool organizer, ensuring you borrow the correct version of the tool and keep it up-to-date.

### pip and pypi
- **pip**: It is the default package manager for Python, allowing you to install, upgrade, and uninstall Python libraries and dependencies from repositories.
- **PyPI**: is the official repository for third-party Python packages. Developers publish their libraries on PyPI, making them accessible to others.
- Pip Installs Packages(pip), Python Package Index (PyPI)

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
