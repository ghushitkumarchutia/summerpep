#  Print numbers from 1 to 20 using while loop

i = 1

while i <= 20:
    print(i)
    i+=1

# Print all even numbers between 1 and 50 using while loop:

i = 1

while i < 50:
    if(i % 2 == 0):
        print(i)
    i+=1

# Take a number n as input
# Print the multiplication table of n till 10

n = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(f"{n} * {i}: {n * i}")
    i += 1

# Take a integer as input
# Count how many digits are present in te number:

number = int(input("Enter a number: "))
digits = 0

while number > 0:
    number = number // 10
    digits +=1

print(f"Number of digits: {digits}")

# Take a number as input
# Reverse the number

number = int(input("Enter a number: "))
reversed_number = 0

while number > 0:
    digits = number % 10
    reversed_number = reversed_number * 10 + digits
    number = number // 10

print(f"The reversed number is : {reversed_number}")

# # Take a number as input
# Check it is palindrome or not

number = int(input("Enter a number: "))

original_number = number
reverse_number = 0

while number > 0:
    digits = number % 10
    reverse_number = reverse_number * 10 + digits
    number = number // 10

if original_number == reverse_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")



# Take a number as input
#  Find the sum if all its digits

number = int(input("Enter a number: "))
sum = 0

while number > 0:
    digits = number % 10
    sum = sum + digits
    number = number // 10

print(f"The sum of all digits is : {sum}")

# Keep taking input from the user
# If user enters 0, stop taking inputs

number = int(input("Enter a number: "))

while number != 0:
    number = int(input("Enter a number: "))

print("Stoped cause you enetered 0!!!")

# Print numbers from 1 to 20
# Skip muliples of 3

i = 1

while i <= 20:
    if i % 3 != 0:
        print(i)
    i += 1

# Print numbers from 1 onwards
# Skip multiple of 4
# Stop the loop whn number becomes greater than 20

i = 1

while i <= 20:
    if i % 4 != 0:
        print(i)
    i += 1