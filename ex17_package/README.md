## 1. The Directory Structure

First, organize your files. Assuming your package is named `timer_utility`, your folder should look like this:

Plaintext

```
timer_utility_project/
├── timer_utility/          # The actual package folder
│   ├── __init__.py         # Makes the folder a package
│   └── decorator.py        # Contains your timing logic
├── tests/                  # Unit tests
├── pyproject.toml          # Build system and metadata
└── README.md               # Documentation
```

## 2. The Code Logic

In `timer_utility/decorator.py`, write your core logic. Using `functools.wraps` is essential to ensure the decorated function keeps its identity (name, docstrings).

```python
import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ...
```

In your `__init__.py`, import the decorator so users can access it easily:

Python

```python
from .decorator import timeit
```

## 3. Configure the Build (`pyproject.toml`)

Modern Python packaging uses `pyproject.toml` instead of the old `setup.py`. This file tells tools like `pip` how to install your code.

TOML

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "timer_utility"
version = "0.1.0"
description = "A simple decorator based package to determine function execution time"
readme = "README.md"
requires-python = ">=3.10"


authors = [
    {name = "Your Name", email = "your@email.com"}
]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
]

dependencies = [
    "numpy<2",
]


[project.scripts]
# CommandName = "FileName:FunctionName"
timer-run = "main:main"
```

## 4. Create a Virtual environment in the folder with the above files (timer_utility_project)

```bash
python -m venv venv
source venv/bin/activate
```


## 5. Build and Install Locally

Before uploading it anywhere, you should test that it installs correctly in your environment.

1. **Navigate** to the root folder (`timer_utility_project/`).

2. **Install** it in "editable" mode:

   Bash

   ```bash
   pip install -e .
   ```

**Test** it in a Python shell:

Python

```python
from timer_utility import timeit

@timeit
def my_func():
    return sum(range(1000000))

my_func()
```

Substitute my_func() with a function of your choice. 

## 6. Build the Package

You need a tool called `build` to turn your code into a "wheel" (a `.whl` file) and a source distribution (`.tar.gz`).

1. **Install the builder:**

   Bash

   ```
   pip install build
   ```

2. **Run the build command** from your root directory:

   Bash

   ```
   python -m build
   ```

You will now see a `dist/` folder containing your package files.

