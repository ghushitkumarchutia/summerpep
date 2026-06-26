# Print:
#  *
#  *
#  *
#  *
#  *

for i in range(5):
    print("*")

print("================")

# Print:
# *****
# *****
# *****
# *****

for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

print("================")

# Print:
# *
# **
# ***
# ****
# *****

for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()

print("================")

# Print:
# *****
# ****
# ***
# **
# *

for i in range(5):
    for j in range(5-i):
        print("*", end="")
    print()

print("================")

# Print:
# 1
# 12
# 123
# 1234
# 12345

for i in range(1, 6):
    for j in range(i):
        print(j+1, end="")
    print()

print("================")

# Print:
# 12345
# 1234
# 123
# 12
# 1

for i in range(1, 6):
    for j in range(6-i):
        print(j+1, end="")
    print()

print("================")

# Print:
# 11111
# 22222
# 33333
# 44444
# 55555

for i in range(1, 6):
    for j in range(5):
        print(i,end="")
    print()

print("================")

# Print:
# A
# AB
# ABC
# ABCD
# ABCDE

for i in range(65, 70):
    for j in range(65, i + 1):
        print(chr(j), end="")
    print()

# Print:
# 1
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    for j in range(i):
        print(i, end="")
    print()

print("================")

# Print:
# 54321
# 5432
# 543
# 54
# 5

for i in range(1, 6):
    for j in range(5, i - 1, -1):
        print(j, end="")
    print()