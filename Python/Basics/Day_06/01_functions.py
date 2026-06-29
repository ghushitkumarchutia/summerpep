#  Functions:

#  Syntax:
def function_name(parameters):
    """Docstring (optional): Deacribes what the function does."""
    # Function body
    return result

#  Printing functions:
def greet():
    """Prints a greeting message."""
    print("Hello World")

#  CALLING THE FUNCTION
greet()
print(greet.__doc__)

#  Returning values
def add(a, b):
    """Adds two numbers."""
    return a + b

result = add(1, 2)
print(result)

#  Function parameters:
def add(a, b):
    """Adds two numbers."""
    return a + b

result = add(1, 2)
print(result)

print(type(print))
print(type(print()))
# 

print(type(add))
print(type(add(1,2)))

result = add(1,2)
print(type(result))

#  types of parameters: 

#  positional arguments
def add_positional(a, b):
    return a + b

result = add_positional(1, 2)
print(result)

#  keyword arguments
def add_keyword(a, b):
    return a + b

result = add_keyword(a=1, b=2)
print(result)

#  default arguments
def add_default(a, b=2):
    return a + b

result = add_default(1)
print(result)

#  arbitrary arguments (*args)
def add_arbitrary(*args):
    return sum(args)

result = add_arbitrary(1, 2, 3)
print(result)

#  keyword arbitrary arguments (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Luffy", role="Captain")

#  positional only arguments (defined with /)
def add_positional_only(a, b, /):
    return a + b

result = add_positional_only(1, 2)
print(result)

#  keyword only arguments (defined with *)
def add_keyword_only(a, *, b):
    return a + b

result = add_keyword_only(1, b=2)
print(result)