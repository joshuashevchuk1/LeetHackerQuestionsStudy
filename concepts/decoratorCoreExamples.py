# A simple decorator function
def decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")

    return wrapper


# Applying the decorator to a function
@decorator
def greet():
    print("Hello, World!")


greet()

def decorator_name(func):
    def wrapper(*args, **kwargs):
        # Add functionality before the original function call
        result = func(*args, **kwargs)
        # Add functionality after the original function call
        return result
    return wrapper

@decorator_name
def function_to_decorate():
    # Original function code
    pass