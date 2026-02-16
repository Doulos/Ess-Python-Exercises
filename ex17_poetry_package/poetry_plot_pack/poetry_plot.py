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

    # Assuming the function returns a list or tuple of x and y values
    if isinstance(result, (list, tuple)) and len(result) == 2:
      x_values, y_values = result
    else:
      raise ValueError("Function must return a list or tuple of x and y values.")

    plt.plot(x_values, y_values)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title(f"Plot of {func.__name__}")
    plt.grid(True)
    plt.savefig('plot.jpg')

    return result

  return wrapper
