# Python code for fibonacci series

range_number = int(input("Enter the range of the fibonacci series: "))

first_number = 0
second_number = 1

print(first_number)
print(second_number)


for i in range(range_number):
    sum = first_number + second_number
    print(sum)
    first_number = second_number
    second_number = sum