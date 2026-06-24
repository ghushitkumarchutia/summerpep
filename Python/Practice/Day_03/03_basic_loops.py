#  Print 1-10:
for i in range(1,11):
    print(i)

#  Print even numbers:
for i in range(2, 31):
    if i % 2 == 0:
        print(i)

# Print odd numbers:
for i in range(1, 31):
    if i % 2 != 0:
        print(i)

# Print reverse counting:
for i in range(31, 0, -1):
    print(i)

# Multiplication table:
number = int(input("Enter a number: "))
for i in range(1, 11):
    product = number * i
    print(f"{number} X {i} = {product}")

# Sum of first n numbers:
number = int(input("Enter a number: "))
sum = 0

for i in range(number+1):
    sum += i
print(sum)

# Factorial:
number = int(input("Enter a number: "))
factorial = 1

for i in range(1, number+1):
    factorial *= i
print(factorial)

# Count digits. eg: 28765 -> 5
number = int(input("Enter a number: "))
count = 0

for count in range(len(str(number))):
    count += 1
print(count)

# Sum of digitd. eg: 1234 -> 10:
number = int(input("Enter a number: "))
sum = 0

for i in range(number+1):
    sum += i
print(sum)