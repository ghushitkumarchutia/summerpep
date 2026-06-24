# ==========================================================
# PYTHON LOOPS - COMPLETE BEGINNER NOTES
# ==========================================================
#
# A loop is used to execute a block of code repeatedly.
#
# Python has two main loops:
# 1. for loop
# 2. while loop
#
# This file focuses on FOR LOOPS and related concepts.
#
# ==========================================================


# ==========================================================
# BASIC FOR LOOP
# ==========================================================

# Print numbers from 1 to 200

for i in range(1, 201):
    print(i)

# Explanation:
#
# for        -> Keyword used to start a loop
# i          -> Loop variable (stores current value)
# in         -> Connects loop variable with sequence
# range()    -> Generates a sequence of numbers
# :          -> Marks the start of the loop body
#
# range(1, 201) generates:
# 1, 2, 3, 4, 5, ..., 200
#
# Note:
# The ending value (201) is NOT included.
# Therefore the loop stops at 200.


# ==========================================================
# IMPORTANT TERMS
# ==========================================================

# 1. LOOP VARIABLE
#
# The variable that stores the current value
# during each iteration.

for number in range(1, 6):
    print(number)

# Output:
# 1
# 2
# 3
# 4
# 5

# Here:
# number = loop variable


# ----------------------------------------------------------


# 2. ITERABLE
#
# An iterable is an object that contains multiple values
# and can be looped through.

# Examples of iterables:

numbers = [10, 20, 30]
name = "Python"
values = range(1, 6)

# All of the above are iterable objects.

for item in numbers:
    print(item)

# Output:
# 10
# 20
# 30


# ----------------------------------------------------------


# 3. ITERATOR
#
# An iterator is an object that provides values
# one at a time.
#
# Python automatically creates an iterator
# when a loop starts.

numbers = range(1, 6)

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Output:
# 1
# 2
# 3


# Easy Memory Trick:
#
# Iterable = Collection of values
# Iterator = Gives values one by one
#
# Example:
#
# Book   = Iterable
# Reader = Iterator


# ----------------------------------------------------------


# 4. ITERATION
#
# One execution of the loop body is called an iteration.

for i in range(1, 4):
    print(i)

# Iteration 1 -> i = 1
# Iteration 2 -> i = 2
# Iteration 3 -> i = 3

# Total iterations = 3


# ----------------------------------------------------------


# 5. COLON (:)
#
# The colon marks the start of a code block.

for i in range(3):
    print(i)

# Everything indented under the loop
# belongs to the loop.


# ==========================================================
# HOW RANGE() WORKS
# ==========================================================

# Syntax:
#
# range(start, stop, step)
#
# start -> Starting value
# stop  -> Ending value (not included)
# step  -> Increment or decrement


# ----------------------------------------------------------
# Example 1: Start and Stop
# ----------------------------------------------------------

for i in range(1, 6):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5


# ----------------------------------------------------------
# Example 2: Only Stop
# ----------------------------------------------------------

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# ----------------------------------------------------------
# Example 3: Step Size
# ----------------------------------------------------------

for i in range(2, 11, 2):
    print(i)

# Output:
# 2
# 4
# 6
# 8
# 10


# ----------------------------------------------------------
# Example 4: Reverse Counting
# ----------------------------------------------------------

for i in range(10, 0, -1):
    print(i)

# Output:
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


# ==========================================================
# INTERESTING EXAMPLES
# ==========================================================

# ----------------------------------------------------------
# Example 1: Print Squares
# ----------------------------------------------------------

for i in range(1, 6):
    print(i, "->", i * i)

# Output:
# 1 -> 1
# 2 -> 4
# 3 -> 9
# 4 -> 16
# 5 -> 25


# ----------------------------------------------------------
# Example 2: Cube of Numbers
# ----------------------------------------------------------

for i in range(1, 6):
    print(i, "->", i ** 3)

# Output:
# 1 -> 1
# 2 -> 8
# 3 -> 27
# 4 -> 64
# 5 -> 125


# ----------------------------------------------------------
# Example 3: Multiplication Table of 5
# ----------------------------------------------------------

for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")

# Output:
# 5 × 1 = 5
# ...
# 5 × 10 = 50


# ----------------------------------------------------------
# Example 4: Sum of Numbers from 1 to 10
# ----------------------------------------------------------

total = 0

for i in range(1, 11):
    total += i

print("Sum =", total)

# Output:
# Sum = 55


# ----------------------------------------------------------
# Example 5: Count Characters in a String
# ----------------------------------------------------------

text = "Python"

count = 0

for char in text:
    count += 1

print("Characters:", count)

# Output:
# Characters: 6


# ----------------------------------------------------------
# Example 6: Print Each Character
# ----------------------------------------------------------

for char in "Python":
    print(char)

# Output:
# P
# y
# t
# h
# o
# n


# ==========================================================
# NESTED LOOP
# ==========================================================

# A loop inside another loop is called a nested loop.

for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()

# Output:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)


# ==========================================================
# BREAK
# ==========================================================

# break immediately stops the loop.

for i in range(1, 11):
    if i == 5:
        break

    print(i)

# Output:
# 1
# 2
# 3
# 4


# ==========================================================
# CONTINUE
# ==========================================================

# continue skips the current iteration.

for i in range(1, 6):
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

# pass means "do nothing".

for i in range(5):
    pass

# Useful when writing code later.


# ==========================================================
# INTERVIEW QUESTIONS
# ==========================================================

# Q1. Difference between Iterable and Iterator?
#
# Iterable:
#   Collection of values that can be looped through.
#
# Iterator:
#   Gives values one by one.


# Q2. Is range() an iterator?
#
# No.
#
# range() is an iterable.
#
# Python creates an iterator from it internally.


# Q3. What is an iteration?
#
# One execution cycle of a loop.


# Q4. Why is colon (:) used?
#
# To indicate the start of a code block.


# ==========================================================
# QUICK REVISION
# ==========================================================
#
# for       -> Loop keyword
# i         -> Loop variable
# range()   -> Iterable object
# Iterator  -> Gives values one by one
# Iteration -> One cycle of loop execution
# :         -> Starts code block
# break     -> Stops loop immediately
# continue  -> Skips current iteration
# pass      -> Does nothing
#
# Memory Trick:
#
# Iterable  = Collection
# Iterator  = Provider
# Iteration = One Loop Cycle
#
# ==========================================================