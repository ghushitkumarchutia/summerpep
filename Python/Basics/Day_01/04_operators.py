# ==========================================================
#                    PYTHON OPERATORS
# ==========================================================
#
# Python has 7 main types of operators:
#
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison (Relational) Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators
#
# Operator Precedence determines which operation is performed
# first when an expression contains multiple operators.
# ==========================================================


# ==========================================================
# 1. ARITHMETIC OPERATORS
# Used for mathematical calculations.
# ==========================================================

a = 10
b = 3

print("Addition (+):", a + b)          # 13
print("Subtraction (-):", a - b)       # 7
print("Multiplication (*):", a * b)    # 30
print("Division (/):", a / b)          # 3.333...
print("Floor Division (//):", a // b)  # 3
print("Modulus (%):", a % b)           # 1 (remainder)
print("Exponent (**):", a ** b)        # 1000 (10³)


# ==========================================================
# 2. ASSIGNMENT OPERATORS
# Used to assign or update values.
# ==========================================================

x = 10      # Assign

x += 5      # x = x + 5
print("x += 5  ->", x)

x -= 3      # x = x - 3
print("x -= 3  ->", x)

x *= 2      # x = x * 2
print("x *= 2  ->", x)

x /= 4      # x = x / 4
print("x /= 4  ->", x)

x //= 2     # Floor divide and assign
print("x //= 2 ->", x)

x %= 3      # Modulus and assign
print("x %= 3 ->", x)

x **= 2     # Power and assign
print("x **= 2 ->", x)


# ==========================================================
# 3. COMPARISON (RELATIONAL) OPERATORS
# Always return True or False.
# ==========================================================

age = 20

print(age == 20)    # Equal to
print(age != 18)    # Not equal to
print(age > 18)     # Greater than
print(age < 30)     # Less than
print(age >= 20)    # Greater than or equal to
print(age <= 25)    # Less than or equal to


# ==========================================================
# 4. LOGICAL OPERATORS
# Used to combine conditions.
# ==========================================================

is_student = True
has_id = False

print(is_student and has_id)    # True only if both are True
print(is_student or has_id)     # True if at least one is True
print(not is_student)           # Reverses True/False


# ==========================================================
# 5. IDENTITY OPERATORS
# Check whether two variables refer to the SAME object.
# ==========================================================

list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)       # True
print(list1 is list3)       # False

print(list1 is not list3)   # True


# ==========================================================
# 6. MEMBERSHIP OPERATORS
# Check whether a value exists in a sequence or collection.
# ==========================================================

crew = ["Luffy", "Zoro", "Nami"]

print("Luffy" in crew)          # True
print("Sanji" in crew)          # False
print("Sanji" not in crew)      # True


# ==========================================================
# 7. BITWISE OPERATORS
# Work on binary (bit) representations of integers.
# Mostly used in low-level programming.
# ==========================================================

a = 5      # Binary: 0101
b = 3      # Binary: 0011

print("a & b =", a & b)     # AND  -> 1
print("a | b =", a | b)     # OR   -> 7
print("a ^ b =", a ^ b)     # XOR  -> 6
print("~a =", ~a)           # NOT  -> -6
print("a << 1 =", a << 1)   # Left shift  -> 10
print("a >> 1 =", a >> 1)   # Right shift -> 2


# ==========================================================
# OPERATOR PRECEDENCE
# Determines which operation happens first.
# ==========================================================

result = 10 + 2 * 3
print(result)      # 16
# Multiplication (*) happens before addition (+).

result = (10 + 2) * 3
print(result)      # 36
# Parentheses () are evaluated first.
