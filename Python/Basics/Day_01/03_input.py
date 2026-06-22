# ======================================================
#               PYTHON INPUT AND TYPE CASTING
# ======================================================

# IMPORTANT:
# input() ALWAYS returns a string (str), no matter what
# the user types.

# ======================================================
# 1. TAKE INPUT
# ======================================================

name = input("Enter your name: ")
age = input("Enter your age: ")
is_pirate = input("Are you a pirate? (yes/no): ")

# ======================================================
# 2. PRINT THE INPUT
# ======================================================

print("\n----- User Input -----")
print("Name      :", name)
print("Age       :", age)
print("Is Pirate :", is_pirate)

# ======================================================
# 3. TYPE CHECK
# ======================================================

# All values from input() are strings.

print("\n----- Data Types Before Conversion -----")
print(type(name))        # <class 'str'>
print(type(age))         # <class 'str'>
print(type(is_pirate))   # <class 'str'>

# ======================================================
# 4. TYPE CASTING (CONVERSION)
# ======================================================

# Convert age from string to integer.
age = int(age)

# Convert "yes"/"no" to a Boolean value.
is_pirate = is_pirate.lower() == "yes"

# ======================================================
# 5. PRINT AFTER CONVERSION
# ======================================================

print("\n----- After Type Casting -----")
print("Name      :", name)
print("Age       :", age)
print("Is Pirate :", is_pirate)

# ======================================================
# 6. CHECK TYPES AGAIN
# ======================================================

print("\n----- Data Types After Conversion -----")
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(is_pirate))   # <class 'bool'>