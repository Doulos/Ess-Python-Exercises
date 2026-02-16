### 1. Initialize the Project with *Poetry*

Open your terminal and run the following commands to create the project structure and add your specific dependencies.

Bash

```bash
# Create a new project from scratch
poetry new ex17_poetry_package
```

**Poetry** creates the directory structure for the project and also the pyproject.toml file. Poetry defaults to a structure where your code lives in a folder named after your package.

Plaintext

```
ex17_poetry_package/
├── pyproject.toml       # The heart of your project
├── README.md
├── poetry_plot_pack/  # Your source code
│   └── __init__.py
└── tests/
    └── __init__.py
```

Instead of editing the `pyproject.toml` file manually, use the CLI. This ensures Poetry resolves version conflicts immediately. Add following dependencies to pyproject.toml - python 3.10, numpy 1.23 and matplotlib 3.7

Bash

```
# Add a production library
poetry add matplotlib "numpy<2"
```



### 2. Write the Decorator Logic to plot and save a given function

Create a file named `poetry_plot_pack/poetry_plot.py`. This decorator will execute the function (to get data) and then use `matplotlib` to plot the result.



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
        
    result = func(*args, **kwargs)
```

### 3. Creating an Executable (Entry Point)

To make your package runnable via a terminal command (like `run-plot`), open `pyproject.toml` and add this section:

TOML

```
[tool.poetry.scripts]
# This creates a terminal command 'run-plot' that executes main() in main.py
run-plot = "main:main"
```

*This tells Poetry: "When I type `run-plot`, execute the `main` function inside `main.py`."* 



### 4. Running and Installing

Poetry manages its own virtual environment, so you don't need to run `python -m venv`.

| **Task**                     | **Command**                                    |
| ---------------------------- | ---------------------------------------------- |
| **Install everything**       | `poetry install`                               |
| **Run your code**            | `poetry run python my_awesome_package/main.py` |
| **Run your CLI command**     | `poetry run run-plot`                            |
| **Activate the environment** | `poetry shell`                                 |

------


### 5. Use the created package in the main.py file 

```Python
from poetry_plot_pack.poetry_plot import plot_graph
import numpy as np

def main():
    print("Initializing plotting package using Poetry")
    ....
    ```

### 6. Build and Publish package

When you are ready to share your work on **PyPI** (the Python Package Index):

1. **Build the distribution files** (`.whl` and `.tar.gz`):

   Bash

   ```
   poetry build
   ```

2. **Publish to PyPI**:

   Bash

   ```
   poetry publish
   ```

   *(Note: You'll need to configure your PyPI credentials/token first using `poetry config`).*

### Why Poetry?

The biggest advantage here is the `poetry.lock` file. It records the exact version of every single sub-dependency, ensuring that if your code works today, it will work on a teammate's machine six months from now.


