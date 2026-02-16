from poetry_plot_pack.poetry_plot import plot_graph
import numpy as np

def main():
    print("Initializing plotting package using Poetry")
    # Example usage of your package functions
    # Call the decorated function
    x_values = np.linspace(0, 8 * np.pi, 100)
    result = my_function(x_values)
    print("Processing complete!")
    print ("Plot saved as plot.jpg file")
    
@plot_graph
def my_function(x):
  """
  #Returns x and the cosine of x.
  """
  import numpy as np
  y = np.cos(x)
  return x, y    
    

if __name__ == "__main__":
    main()




