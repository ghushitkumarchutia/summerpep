# Python code whether a number palindrome or not

number = int(input("Enter a number: "))

original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

if original_number == reversed_number:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
