# ======================================================
#               PYTHON BUILT-IN DATA TYPES
# ======================================================

# Python has 8 major categories of built-in data types:
#
# 1. Text Type      -> str
# 2. Numeric Types  -> int, float, complex
# 3. Sequence Types -> list, tuple, range
# 4. Mapping Type   -> dict
# 5. Set Types      -> set, frozenset
# 6. Boolean Type   -> bool
# 7. Binary Types   -> bytes, bytearray, memoryview
# 8. None Type      -> NoneType
#
# Mutable   = Can be changed after creation.
# Immutable = Cannot be changed after creation.

# ======================================================
# 1. TEXT TYPE
# ======================================================

name = "Monkey D Luffy"      # str (immutable)
print(name, "|", type(name))


# ======================================================
# 2. NUMERIC TYPES
# ======================================================

age = 19                     # int -> Whole number
price = 99.99                # float -> Decimal number
complex_num = 3 + 5j         # complex -> Real + imaginary

print(age, "|", type(age))
print(price, "|", type(price))
print(complex_num, "|", type(complex_num))


# ======================================================
# 3. SEQUENCE TYPES
# ======================================================

# list -> Ordered, mutable
crew = ["Luffy", "Zoro", "Nami"]

# tuple -> Ordered, immutable
fruit = ("Gomu Gomu no Mi", "Paramecia")

# range -> Sequence of numbers
numbers = range(1, 6)

print(crew, "|", type(crew))
print(fruit, "|", type(fruit))
print(list(numbers), "|", type(numbers))


# ======================================================
# 4. MAPPING TYPE
# ======================================================

# dict -> Key-value pairs, mutable
bounties = {
    "Luffy": 3000000000,
    "Zoro": 1111000000
}

print(bounties, "|", type(bounties))


# ======================================================
# 5. SET TYPES
# ======================================================

# set -> Unordered collection of unique values, mutable
islands = {"Wano", "Alabasta", "Dressrosa"}

# frozenset -> Immutable version of set
important_places = frozenset({"Laugh Tale", "Mariejois"})

print(islands, "|", type(islands))
print(important_places, "|", type(important_places))


# ======================================================
# 6. BOOLEAN TYPE
# ======================================================

# bool -> True or False
# Note: bool is a subclass of int in Python.
is_captain = True

print(is_captain, "|", type(is_captain))


# ======================================================
# 7. BINARY TYPES
# ======================================================

# bytes -> Immutable binary data
data = b"Hello"

# bytearray -> Mutable binary data
mutable_data = bytearray(b"Hello")

# memoryview -> View into binary data without copying
view = memoryview(data)

print(data, "|", type(data))
print(mutable_data, "|", type(mutable_data))
print(view, "|", type(view))


# ======================================================
# 8. NONE TYPE
# ======================================================

# None represents the absence of a value.
result = None

print(result, "|", type(result))