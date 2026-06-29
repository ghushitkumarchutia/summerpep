# Create a function greet the students

def greet(student_name):
    print("Welcome",student_name,"!!")

#
greet("Alex")
greet("Bob")
greet("Charlie")
greet("David")
greet("Eve")

#  Calculator
def calculator(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    elif operation == "sq":
        return num1 * num1
    elif operation == "cube":
        return num1 * num1 * num1
    elif operation == "%":
        return num1 % num2
    elif operation == "//":
        return num1 // num2
    else:
        return "Invalid operation"

print(calculator(10, 2, "+"))
print(calculator(10, 2, "-"))
print(calculator(10, 2, "*"))
print(calculator(10, 2, "/"))
print(calculator(10, 2, "sq"))
print(calculator(10, 2, "cube"))
print(calculator(10, 2, "%"))
print(calculator(10, 2, "//"))
print(calculator(10, 2, "xyz"))

# Check largest number out of two numbers
def largest(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Both numbers are equal"

print(largest(10, 2))
print(largest(2, 10))
print(largest(10, 10))

# Check even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(check_even_odd(48))
print(check_even_odd(71))

# Check largest number among 5 numbers
def largest_5(num1, num2, num3, num4, num5):
    max_num = num1
    if num2 > max_num:
        max_num = num2
    if num3 > max_num:
        max_num = num3
    if num4 > max_num:
        max_num = num4
    if num5 > max_num:
        max_num = num5
    return max_num

print(largest_5(10, 2, 5, 8, 3))
print(largest_5(2, 10, 5, 8, 3))
print(largest_5(5, 10, 2, 8, 3))

# Functions using each 5 parameters need to be different from each others

# Positional Arguments
def positional(a, b, c):
    return a + b + c

print(positional(10, 2, 5))

# Keyword Arguments
def keyword(first, second, third):
    return f"{first} -> {second} -> {third}"

print(keyword(first="A", second="B", third="C"))

# Default parameters
def default(name="Guest", is_logged_in=False):
    if is_logged_in:
        print("Welcome",name,"!!")
    else:
        print("Welcome Guest!!")

default("Luffy", True)
default()

# Arbitrary arguments
def arbitrary(*args):
    return sum(args)

print(arbitrary(1, 2, 3))
print(arbitrary(1, 2, 3, 4, 5))

# Keyword Arbitrary arguments
def keyword_arbitrary(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

keyword_arbitrary(name="Luffy", role="Captain")
