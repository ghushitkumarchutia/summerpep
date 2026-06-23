# Conditional statement : 

# Voting eligibility using conditional statement
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Positive and Negative number using conditional statement
number = int(input("Enter your number: "))

if number == 0:
    print("Number is zero")
elif number > 0:
    print("It is a positive number")
else:
    print("It is a negative number")

# Categorize employees based on salaries
employee_salary = int(input("Enter your salary: "))

if employee_salary <=0:
    print("Salary cannot be zero or negative.")
elif employee_salary < 30000:
    print("Employee is in the lower salary bracket")
elif employee_salary < 50000:
    print("Employee is in the middle salary bracket")
elif employee_salary < 70000:
    print("Employee is in the upper salary bracket")
else:
    print("Employee is in the high salary bracket")

# Check prime number or not
number = int(input("Enter your number: "))

if number <=1:
    print("Number is not prime.")
else:
    is_prime = True

    for i in range(2, number):
        if(number % i == 0):
            is_prime = False
            break

    if is_prime:
        print("Number is prime.")
    else:
        print("Number is not prime.")