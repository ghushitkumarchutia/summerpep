# Calculator
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /, %, **): ")

if operator == "+":
    print("Result of {num1} + {num2}: ",num1 + num2)
elif operator == "-":
    print("Result of {num1} - {num2}: ",num1 - num2)
elif operator == "*":
    print("Result of {num1} * {num2}: ",num1 * num2)
elif operator == "/":
    print("Result of {num1} / {num2}: ",num1 / num2)
elif operator == "%":
    print("Result of {num1} % {num2}: ",num1 % num2)
elif operator == "**":
    print("Result of {num1} ** {num2}: ",num1 ** num2)
else:
    print("Invalid operator")