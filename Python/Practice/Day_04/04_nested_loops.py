#  Print following outputs:
# 0 0
# 0 1
# 0 2
# 1 1
# 1 2
# 2 0
# 2 1
# 2 2

for i in range(3):
    for j in range(3):
        if not (i == 1 and j == 0):
            print(i, j)
    
# Print the following:
# Row 1:
#       Column 1
#       Column 2
#       Column 3
# Row 2:
#       Column 1
#       Column 2
#       Column 3
# Row 3:
#       Column 1
#       Column 2
#       Column 3

for i in range(3):
    print(f"Row {i+1}:")
    for j in range(3):
        print(f"      Column {j+1}")

# Print the following:
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

for i in range(3):
    for j in range(1, 5):
        print(j, end=" ")
    print()

# Print the following:
#  A B C D
#  A B C D
#  A B C D
#  Hint: use chr()

for i in range(3):
    for j in range(1, 5):
        print(chr(64+j), end=" ")
    print()

# Print the multiplication table 
# 1 2 3
# 2 4 6
# 3 6 9

for i in range(1, 4):
    for j in range(1, 4):
        print(i*j, end=" ")
    print()

# Print the following
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4

for i in range(1, 5):
    for j in range(1, 5):
        print(i, end=" ")
    print()

# Print the following:
# 1 2 3
# 4 5 6
# 7 8 9

num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()

# Print the following:
# 2 4 6
# 8 10 12
# 14 16 18

num = 2
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 2
    print()

# Predict the output:
for i in range(3):
    for j in range(2):
        print(i, j, end="")

# Output: 0 00 11 01 12 02 1