'''
Instructions
Create a logging_decorator() which is going to print the name of the function that was called, the arguments
it was given and finally the returned output:

You called a_function(1,2,3)
It returned: 6
The value 6 is the return value of the function. Don't change the body of a_function.

IMPORTANT: You only need to use *args, you can ignore **kwargs in this exercise.

Example Input
[1,2,3]
Example Output
You called a_function(1,2,3)
It returned: 6
Hint
You can use function.__name__ to get the name of the function.

Use *args.
'''

inputs = [1, 2, 3]
inputs = [1, 2, 3]

# Create the logging_decorator() function
def logging_decorator(funt):
    def wrapper(*args):
        print(f"You called {funt.__name__}{args}")
        result = funt(*args)
        print(f"It returned: {result}")
        return result
    return wrapper

# Use the decorator
@logging_decorator
def a_function(a, b, c):
    return a * b * c

# Call the decorated function
a_function(inputs[0], inputs[1], inputs[2])

'''

Explanation:
logging_decorator:

The wrapper function inside the decorator takes any number of arguments (*args).
It prints the name of the function being called (funt.__name__) and the arguments passed to it.
It then calls the original function funt with those arguments and stores the result.
It prints the result and returns it.
a_function:

This is the original function that multiplies three arguments.
It is decorated with logging_decorator, so when called, it will first execute the logging logic in the decorator.
Calling the decorated function:

a_function(inputs[0], inputs[1], inputs[2]) calls the decorated version of a_function.
The decorator prints the function name and arguments, calls the original function, prints the result, and returns the result.
'''