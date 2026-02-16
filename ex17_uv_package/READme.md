### 1.The Directory Structure

First, organize your files. Assuming your package is named `plot_uv_pkg`, your folder should look like this:

Plaintext

```
ex_17_uv_package/
├── plot_uv_pkg/          # The actual package folder
│   ├── __init__.py         # Makes the folder a package
│   └── decorator.py        # Contains your timing logic
├── tests/                  # Unit tests
├── pyproject.toml          # Build system and metadata
└── README.md               # Documentation
```

### 2. The Code Logic

In `plot_uv_pkg/decorator.py`, write your core logic. 

```python
import matplotlib.pyplot as plt
import numpy as np

def plot_graph(func):
  """
  Decorator to plot the output of a function using matplotlib.
  Args:
    func: The function to decorate.
  Returns:
    A function that calls the original function and plots its output.
  """
  def wrapper(*args, **kwargs):
```

In your `__init__.py`, import the decorator so users can access it easily:

Python

```python
from .decorator import timeit
```



### 3. Configure the Build (`pyproject.toml`)

Modern Python packaging uses `pyproject.toml` instead of the old `setup.py`. This file tells tools like `pip` how to install your code.

TOML

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "plot_uv_pkg"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "matplotlib>=3.10.8",
    "numpy<2",
]
```

### 4. Initialize the Project with `uv`  (optional: You could use this or steps 1 and 3 above)

Open your terminal and run the following commands to create the project structure and add your specific dependencies.

Bash

```bash
# Create the project structure
uv init plot_uv_pkg
cd plot_decorator_pkg

# Add dependencies with your specific constraints
uv add "numpy<2" matplotlib
```

**uv init** creates the directory structure for the project and also the pyproject.toml file. The **uv add** command updates the pyproject.toml file dependency section.  The attributes of pyproject.toml configuration file are common across different packaging platforms.  Refer to this [webpage](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/#writing-pyproject-toml) for more details on writing your own pyproject.toml file. 

### 5. Build the editable and Wheel Files

```bash
uv sync
```

This creates an editable package that can be viewed using **uv tree**

uv` uses the `build` backend defined in your `pyproject.toml`. To generate the `.whl` file, run:

Bash

```
uv build
```

This will create a `dist/` folder containing two files:

1. `plot_uv_pkg-0.1.0-py3-none-any.whl` (The Wheel)
2. `plot_ur_pkg-0.1.0.tar.gz` (The Source Dist)

In your `__init__.py`, import the decorator so users can access it easily:

Python

```python
from .decorator import timeit
```



### 6. Call the package in a main.py file to execute plot_graph function

This main.py is outside the package folder, and is at the same level as pyproject.toml file

```python
from plot_uv_pkg.decorator import plot_graph
import numpy as np

def main():
    print("Initializing plotting package using UV")
    # Example usage of your package functions
```



### 7. UV "Zero-Setup" Workflow

With UV installed, there is no need to create a venv or install requirements. You simply type:

Bash

```bash
uv run main.py
```

`uv` will detect the missing environment, create it, install `numpy<2` and `matplotlib`, and launch the plot all in one go.



------

### Table of `uv` commands used

| **Command**        | **Purpose**                                       | **Primary File Affected**           |
| ------------------ | ------------------------------------------------- | ----------------------------------- |
| **`uv init`**      | **Start** a new project from scratch.             | `pyproject.toml`, `.python-version` |
| **`uv add <pkg>`** | **Add** a new library to the project.             | `pyproject.toml` & `uv.lock`        |
| **`uv sync`**      | **Align** the local `.venv` with the lockfile.    | `.venv` folder                      |
| **`uv run <cmd>`** | **Execute** code using the project's environment. | None (Execution only)               |

 