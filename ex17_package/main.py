from timer_utility import timeit

def main():
    print("Initializing timing package")
    # Example usage of your package functions
    # Call the decorated function    
    my_func()    
    print("Processing complete!")
   
    
@timeit
def my_func():
    return sum(range(1000000))

 
  

if __name__ == "__main__":
    main()




