# ==========================================================
# PYTHON WHILE LOOP - COMPLETE BEGINNER NOTES
# ==========================================================
#
# A while loop executes a block of code repeatedly
# as long as a condition remains True.
#
# Python has two main loops:
# 1. for loop
# 2. while loop
#
# This file focuses on WHILE LOOPS and related concepts.
#
# ==========================================================


# ==========================================================
# BASIC WHILE LOOP
# ==========================================================

# Print numbers from 1 to 10

number = 1

while number <= 10:
    print(number)
    number += 1

# Explanation:
#
# while      -> Keyword used to start a while loop
# number <= 10 -> Condition
# :          -> Marks the start of loop body
# number += 1 -> Updates the loop variable
#
# The loop continues while the condition is True.
#
# When number becomes 11:
#
# 11 <= 10
#
# becomes False and the loop stops.


# ==========================================================
# IMPORTANT TERMS
# ==========================================================

# 1. LOOP VARIABLE
#
# A variable whose value changes during each iteration.

count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5

# Here:
# count = loop variable


# ----------------------------------------------------------


# 2. CONDITION
#
# A condition decides whether the loop should continue.

age = 1

while age <= 3:
    print(age)
    age += 1

# The condition is:
#
# age <= 3
#
# If True  -> Continue loop
# If False -> Stop loop


# ----------------------------------------------------------


# 3. ITERATION
#
# One execution of the loop body.

i = 1

while i <= 3:
    print(i)
    i += 1

# Iteration 1 -> i = 1
# Iteration 2 -> i = 2
# Iteration 3 -> i = 3

# Total iterations = 3


# ----------------------------------------------------------


# 4. COLON (:)
#
# Colon marks the start of the code block.

i = 1

while i <= 3:
    print(i)
    i += 1

# Everything indented belongs to the loop.


# ----------------------------------------------------------


# 5. INCREMENT
#
# Increment means increasing a value.

count = 1

while count <= 5:
    print(count)
    count += 1

# count += 1
#
# is equivalent to:
#
# count = count + 1


# ----------------------------------------------------------


# 6. DECREMENT
#
# Decrement means decreasing a value.

count = 5

while count >= 1:
    print(count)
    count -= 1

# count -= 1
#
# is equivalent to:
#
# count = count - 1


# ==========================================================
# HOW A WHILE LOOP WORKS
# ==========================================================

number = 1

while number <= 3:
    print(number)
    number += 1

# Step 1:
#
# number = 1
#
# 1 <= 3 -> True
#
# Output: 1
#
# number becomes 2


# Step 2:
#
# 2 <= 3 -> True
#
# Output: 2
#
# number becomes 3


# Step 3:
#
# 3 <= 3 -> True
#
# Output: 3
#
# number becomes 4


# Step 4:
#
# 4 <= 3 -> False
#
# Loop stops


# ==========================================================
# INTERESTING EXAMPLES
# ==========================================================

# ----------------------------------------------------------
# Example 1: Print Numbers 1 to 10
# ----------------------------------------------------------

i = 1

while i <= 10:
    print(i)
    i += 1


# ----------------------------------------------------------
# Example 2: Reverse Counting
# ----------------------------------------------------------

i = 10

while i >= 1:
    print(i)
    i -= 1

# Output:
# 10
# 9
# 8
# ...
# 1


# ----------------------------------------------------------
# Example 3: Multiplication Table of 5
# ----------------------------------------------------------

i = 1

while i <= 10:
    print(f"5 × {i} = {5 * i}")
    i += 1


# ----------------------------------------------------------
# Example 4: Sum of Numbers 1 to 10
# ----------------------------------------------------------

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum =", total)

# Output:
# Sum = 55


# ----------------------------------------------------------
# Example 5: Count Digits
# ----------------------------------------------------------

number = 28765

count = 0

while number > 0:
    number //= 10
    count += 1

print("Digits =", count)

# Output:
# Digits = 5


# ----------------------------------------------------------
# Example 6: Sum of Digits
# ----------------------------------------------------------

number = 1234

digit_sum = 0

while number > 0:
    digit_sum += number % 10
    number //= 10

print("Sum =", digit_sum)

# Output:
# Sum = 10


# ----------------------------------------------------------
# Example 7: Print Even Numbers
# ----------------------------------------------------------

i = 2

while i <= 20:
    print(i)
    i += 2

# Output:
# 2 4 6 8 10 12 14 16 18 20


# ==========================================================
# INFINITE LOOP
# ==========================================================

# A loop that never stops.

# while True:
#     print("Hello")

# This loop runs forever because
# the condition is always True.


# ==========================================================
# BREAK
# ==========================================================

# break immediately stops the loop.

i = 1

while True:
    if i == 5:
        break

    print(i)
    i += 1

# Output:
# 1
# 2
# 3
# 4


# ==========================================================
# CONTINUE
# ==========================================================

# continue skips the current iteration.

i = 0

while i < 5:
    i += 1

    if i == 3:
        continue

    print(i)

# Output:
# 1
# 2
# 4
# 5


# ==========================================================
# PASS
# ==========================================================

# pass means do nothing.

i = 1

while i <= 5:
    pass
    break

# Useful when writing code later.


# ==========================================================
# NESTED WHILE LOOP
# ==========================================================

row = 1

while row <= 3:

    col = 1

    while col <= 3:
        print(f"({row},{col})", end=" ")
        col += 1

    print()
    row += 1

# Output:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)


# ==========================================================
# COMMON MISTAKE
# ==========================================================

# Forgetting to update the loop variable.

# Wrong:

# i = 1
#
# while i <= 5:
#     print(i)

# Infinite loop because i never changes.


# Correct:

i = 1

while i <= 5:
    print(i)
    i += 1


# ==========================================================
# WHEN TO USE WHILE LOOP
# ==========================================================

# Use while when:
#
# 1. Number of iterations is unknown.
#
# 2. You only know the stopping condition.
#
# 3. Input validation.
#
# 4. ATM systems.
#
# 5. Menu-driven programs.
#
# 6. Games.
#
# 7. Password checking.
#
# 8. Reading data until a condition is met.
#
# 9. Infinite loops.


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

# Q1. Difference between for and while?
#
# for:
#   Used when number of iterations is known.
#
# while:
#   Used when stopping condition is known.


# Q2. What is an infinite loop?
#
# A loop that never ends.


# Q3. Why is increment important?
#
# To eventually make the condition False
# and stop the loop.


# Q4. Can while loop run zero times?
#
# Yes.

number = 10

while number < 5:
    print(number)

# Output:
# Nothing

# Condition is False initially.


# ==========================================================
# QUICK REVISION
# ==========================================================
#
# while      -> Loop keyword
# condition  -> Controls loop execution
# iteration  -> One cycle of execution
# increment  -> Increase value
# decrement  -> Decrease value
# :          -> Starts code block
# break      -> Stops loop immediately
# continue   -> Skips current iteration
# pass       -> Does nothing
#
# Memory Trick:
#
# for   -> Known repetitions
# while -> Known condition
#
# ==========================================================