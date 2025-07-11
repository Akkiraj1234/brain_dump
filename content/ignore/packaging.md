# Packaging in Python
Packaging refers to organizing your project so it can be shared, installed, and used by others. It often involves grouping multiple modules into a package (a directory with an `__init__`.py file).

1. **Reusability**: When you write Python code, packaging allows you to share your code as a reusable module or library.
2. **Dependency Management**: Packaging tools like pip  allow you to manage dependencies, and libraries or versions of libraries are installed correctly. 
3. **Ease of Installation**: Packaging ensures that software can be installed with a simple command like `pip install <package>`
4. Packaging ensures that Python applications can be used across multiple operating systems.

## issues you will face if not using packaging tools
1. Dependency Conflicts (Dependency Hell) 
2. Difficulty in Managing Multiple Projects
3. Version Management Issues
4. Difficulty in Reproducing Environments (Reproducibility)
5. Poor Collaboration and Teamwork

## packaging tecnlogyies required
1. pypi
2. pip
3. poetry


## The minmul Python Package strctuture
```bash
my_library/
├── my_library/
│   ├── __init__.py  # Makes it a package
│   ├── core.py      # Core logic
│   ├── utils.py     # Helper functions
├── tests/           # Unit tests
│   ├── test_core.py
├── README.md        # Project description
├── pyproject.toml   # Modern build configuration
├── LICENSE          # License for usage
└── setup.cfg        # Optional additional setup configuration
```
### **Key Files**:
- pyproject.toml: Defines project metadata, dependencies, and build-backend.
- README.md: For documentation (used by PyPI).
- LICENSE: Specifies the license.
### **Tool to Use**: Poetry or setuptools.
### **Example Command to Build:**
```bash
poetry build
poetry publish
```







# pip 
A tool that automates the process of installing, upgrading, configuring, and managing software libraries or dependencies.
- Simplifies dependency management by allowing you to specify packages needed for a project.
- why its needed imagin u building a app that fatch html conetent from a link for that u can either write all the https request protocole and code or just download a library that written by a profestion like request by simple command `pip install request` that will download it in the System's site-packages Directory and after u can import it in ur module or package import request.

## warning read this first :
1. migration, Linux users using the system Python without creating a virtual
   environment first should replace the ``python`` command in this tutorial
   with ``python3`` and the ``python -m pip`` command with ``python3 -m pip --user``. Do *not*
   run any of the commands in this tutorial with ``sudo``: if you get a
   permissions error, come back to the section on creating virtual environments,
   set one up, and then continue with the tutorial as written.
   1. creation
        ```bash
        ::unix or mac
        python3 -m venv tutorial_env
        ::window
        python -m venv tutorial_env
        ```
   2. activate
        ```bash
        ::unix or mac
        source tutorial_env/bin/activate
        ::window
        tutorial_env\Scripts\activate
        ```
   3. exit
        ```bash
        ::unix or mac and window
        deactivate
        ```

## ensure if pip installed or not
```shell
::Unix/macOS
python3 -m pip --version
```
```bat
::Windows
python -m pip -- verstion
```
### if pip not installed then follow the tutorial
- install python from [python.org](https://python.org) and install it with customize installation option and mark the pip and install the python
- install it visa python by bootsraping it
    ```bash
    ::unix or mac
    python3 -m ensurepip --default-pip
    ::window
    python -m ensurepip --default-pip
    ```
- else install pip from here manually [get-pip](https://bootstrap.pypa.io/get-pip.py) this will install **pip**, **setuptools**, **wheel**

## Installing from PyPI with pip
### To install the latest version of "SomeProject":
```bash
python -m pip install "SomeProject"
```
### To install a specific version:
```bash
python -m pip install "SomeProject==1.4"
```
### To install greater than or equal to one version and less than another:
```bash
python -m pip install "SomeProject>=1,<2"
```
### To install a version that's compatible with a certain version
```bash
python -m pip install "SomeProject~=1.4.2"
```
## Upgrading packages
Upgrade an already installed ``SomeProject`` to the latest from PyPI.
```bash
python -m pip install --upgrade SomeProject
```
## Installing to the User Site
To install packages Distribution Package that are isolated to the
current user, use the `--user` flag:
```bash
python -m pip install --user SomeProject
```
#### Note that the ``--user`` flag has no effect when inside a virtual environment

If ``SomeProject`` defines any command-line scripts or console entry points,
``--user`` will cause them to be installed inside the `user base`_'s binary
directory, which may or may not already be present in your shell's
:envvar:`PATH`.  (Starting in version 10, pip displays a warning when
installing any scripts to a directory outside :envvar:`PATH`.)  If the scripts
are not available in your shell after installation, you'll need to add the
directory to your :envvar:`PATH`:

On Windows you can find the user base binary directory by running ``py -m
  site --user-site`` and replacing ``site-packages`` with ``Scripts``. For
  example, this could return
  ``C:\Users\Username\AppData\Roaming\Python36\site-packages`` so you would
  need to set your ``PATH`` to include
  ``C:\Users\Username\AppData\Roaming\Python36\Scripts``. You can set your user
  ``PATH`` permanently in the `Control Panel`_. You may need to log out for the
  ``PATH`` changes to take effect.

## Installing from VCS
Install a project from VCS in "editable" mode.
```bat
python -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git          :: from git
python -m pip install -e SomeProject @ hg+https://hg.repo/some_pkg                :: from mercurial
python -m pip install -e SomeProject @ svn+svn://svn.repo/some_pkg/trunk/         :: from svn
python -m pip install -e SomeProject @ git+https://git.repo/some_pkg.git@feature  :: from a branch
```

## Installing from other Indexes
Install from an alternate index
```bash
python -m pip install --index-url http://my.package.repo/simple/ SomeProject
```
covere --extra-index too

## Installing from a local src tree
in such a way that the project appears to be installed, but yet is
still editable from the src tree.
```bash
python -m pip install -e <path>
```
You can also install normally from src
```bash
python -m pip install <path>
```

## Installing from local archives
python -m pip install ./downloads/SomeProject-1.0.4.tar.gz

## Installing Prereleases
Find pre-release and development versions, in addition to stable versions.  By
default, pip only finds stable versions.
```bash
python3 -m pip install --pre SomeProject
```

## Installing "Extras"
python3 -m pip install 'SomePackage[PDF]'
python3 -m pip install 'SomePackage[PDF]==3.0'

## Requirements files
Install a list of requirements specified in a Requirements.txt fille

### why:
the need of Requirements fille is to create the same enviormnt to run ur script on other devies

```bash
python -m pip install -r requirements.txt
```
- A plain text file listing the dependencies for a Python project.
- Each line specifies a package and optionally its version constraints

```bash
requests>=2.25.1
numpy==1.23.1
```
### Using pip freeze and pip install for Dependency Management
- pip freeze: Outputs a list of installed packages and their versions.
        Example: pip freeze > requirements.txt creates a requirements.txt file.
-pip install -r requirements.txt: Installs dependencies from a requirements.txt file.

