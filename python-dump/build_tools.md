**[`back`](./_content_.md)**

# **Build Tools: Learn Build Tools**

This guide introduces essential tools for managing and enhancing Python projects.  


1. **Project Management**
   - **`Poetry`**:  dependency management and project packaging tool.
   - **`pyproject.toml`**: Central configuration for build tools.

2. **Static Typing**
   - **`typing`**: Built-in Python module for type hints.
   - **`mypy`**: A static type checker for Python.

3. **Code Formatting**
   - **[`yapf`](#yapf-yet-another-python-formatter)**: Automatic code formatter.
   - **[`black`](#black-python-code-formatter)**: "The uncompromising code formatter."


## [**YAPF (Yet Another Python Formatter)**](https://github.com/google/yapf)
YAPF focuses on reformatting Python code to match a specific style guide (like **PEP 8**) or a custom configuration. It ensures clean, consistent, and professional code. YAPF supports **Python 3.7+**.

### **Key Arguments**
- **positional arguments**: **fille** or else read from **stdin**
- `-i` or `--in-place`: Format the file directly.
- `--diff`: Show differences without modifying files.
- `--style`: Specify a style (e.g., `--style=pep8` or `--style=.style.yapf`).
- `--recursive`: Format files in subdirectories.
- `--parallel`: run YAPF in parallel when formatting multiple files.
- `--verbose`: print out file names while processing.
- `-help`: show this help message and exit.

---

### **Code Examples**

#### **Installation**
```bash
# Install YAPF using pip:
pip install yapf
```
For editor integration, refer to [editor_support](https://github.com/google/yapf/blob/main/EDITOR%20SUPPORT.md)

#### **Usage**
- Format a Python file:
    ```bash
    yapf your_file.py
    ```
- Overwrite a file with formatted code:
    ```bash
    yapf -i your_file.py
    ```
- Format an entire directory recursively:
    ```bash
    yapf -r -i path/to/your/code
    ```
- Format a string of code (via piping):
    ```bash
    echo "x= {1,2 ,3}" | yapf
    ```

---
### Configuring YAPF

YAPF can be configured using a `.style.yapf file`, `pyproject.toml`, or `setup.cfg`

- example of **.style.yapf**
    ```ini
    [style]
    based_on_style = pep8
    column_limit = 80
    indent_width = 4
    ```
- example of **pyproject.toml**
    ```ini
    [tool.yapf]
    based_on_style = "pep8"
    column_limit = 80
    indent_width = 4
    ```

---
### Customizing YAPF Styles
YAPF provides extensive customization options. Here are some examples:
| **Option**                     | **Type** | **Description**                                             |
|--------------------------------|----------|-------------------------------------------------------------|
| `based_on_style`               | `str`    | Base style: `pep8`, `google`, `chromium`, `facebook`.       |
| `column_limit`                 | `int`    | Maximum characters per line. Default: `80`.                |
| `indent_width`                 | `int`    | Number of spaces per indentation. Default: `4`.            |
| `split_before_logical_operator`| `bool`   | Split lines before logical operators (`and`, `or`).         |
| `coalesce_brackets`            | `bool`   | Combine closing brackets with the last element.            |
| `allow_split_before_dict_value`| `bool`   | Allow line splits before dictionary values.                |
### To view all options, run:
```bash
yapf --style-help
```
For more, check the style [kanob](https://github.com/google/yapf?tab=readme-ov-file#knobs).

---
### Integration with VS-Code
1. Install EeyoreLee's yapf extension.
2. Install the yapf package from pip.
    ```
    pip install yapf
    ```
3. Add the following to VSCode's `settings.json`:
    ```json
    "[python]": {
        "editor.formatOnSaveMode": "file",
        "editor.formatOnSave": true,
        "editor.defaultFormatter": "eeyore.yapf"  
    },
    ```

## [**Black: Python Code Formatter**](https://github.com/psf/black)
Black is an opinionated code formatter that enforces a single consistent style for Python code with minimal configuration, with minimal learning curve.

### **Key Features:**
- **Opinionated**: Black has very few customization options. It removes debates about style.
- **Fast**: Optimized for speed.
- **Deterministic**: Always formats code the same way.

### Installation:
```bash
pip install black
```

### Basic Commands:
```bash
# Format a file
black your_file.py

# Format a directory recursively
black path/to/your/code --recursive

# Check code formatting (without modifying files)
black --check your_file.py

# Show diffs (without applying changes)
black --diff your_file.py

# Change max line length (default: 88)
black --line-length 100 your_file.py

# Skip string normalization (don't change quotes)
black --skip-string-normalization your_file.py

# Target specific Python version
black --target-version py38 your_file.py
```

### Configuration Options (minimal customization):
- Line length: Change the max characters per line (default is 88):
    ```bash
    black --line-length 100 your_file.py
    ```
- Skip string normalization (don't change quotes):
    ```bash
    black --skip-string-normalization your_file.py
    ```
- Target specific Python versions:
    ```bash
    black --target-version py38 your_file.py
    ```

### Using Black in VSCode:
1. install black : run **pip install black**
2. Set Black as the default formatter:
   - Open settings.json in VSCode and add:
    ```json
    {
        "python.formatting.provider": "black",
        "editor.formatOnSave": true,
        "python.formatting.blackArgs": [
            "--line-length", "100"
        ]
    }
    ```
3. Enable format-on-save: In VSCode, search for Editor: Format On Save in settings and enable it.

### u can also set it in Pre-commit Hook (automate Black in git workflows) and CI/CD Integration: