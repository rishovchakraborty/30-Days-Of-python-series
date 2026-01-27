
# ============================================================
# 1️⃣ SYNTAX ERROR
# ============================================================

# ❌ SyntaxError happens when Python cannot understand your code structure
# This error occurs BEFORE the program runs

# Uncomment the below code to see SyntaxError

# if True
#     print("Hello")

"""
ERROR:
SyntaxError: invalid syntax

WHY?
- Missing colon (:) after if True
"""

# ============================================================
# 2️⃣ RUNTIME ERRORS (EXCEPTIONS)
# ============================================================
# These occur while the program is running

# ------------------------------------------------------------
# a) ZeroDivisionError
# ------------------------------------------------------------

try:
    x = 10 / 0
except ZeroDivisionError:
    print("ZeroDivisionError: You cannot divide by zero")


# ------------------------------------------------------------
# b) NameError
# ------------------------------------------------------------

try:
    print(age)
except NameError:
    print("NameError: Variable 'age' is not defined")


# ------------------------------------------------------------
# c) TypeError
# ------------------------------------------------------------

try:
    result = "10" + 5
except TypeError:
    print("TypeError: Cannot add string and integer")


# ------------------------------------------------------------
# d) ValueError
# ------------------------------------------------------------

try:
    num = int("abc")
except ValueError:
    print("ValueError: Cannot convert 'abc' to int")


# ------------------------------------------------------------
# e) IndexError
# ------------------------------------------------------------

try:
    numbers = [1, 2, 3]
    print(numbers[5])
except IndexError:
    print("IndexError: List index out of range")


# ------------------------------------------------------------
# f) KeyError
# ------------------------------------------------------------

try:
    student = {"name": "Rishov", "age": 21}
    print(student["marks"])
except KeyError:
    print("KeyError: Key does not exist in dictionary")


# ------------------------------------------------------------
# g) AttributeError
# ------------------------------------------------------------

try:
    name = "Rishov"
    name.append("C")
except AttributeError:
    print("AttributeError: Strings do not have append()")


# ------------------------------------------------------------
# h) FileNotFoundError
# ------------------------------------------------------------

try:
    file = open("missing_file.txt", "r")
except FileNotFoundError:
    print("FileNotFoundError: File does not exist")


# ============================================================
# 3️⃣ LOGICAL ERROR
# ============================================================
# No error message ❗
# Program runs but gives WRONG output

# Example: Calculate average

marks = [80, 90, 70]
total = 0

for m in marks:
    total += m

# ❌ Logical mistake (dividing by 2 instead of 3)
average = total / 2

print("Average marks:", average)

"""
EXPECTED OUTPUT:
80.0

ACTUAL OUTPUT:
120.0

WHY?
- Wrong formula used
- Python cannot detect logical errors
"""

# ============================================================
# 4️⃣ CUSTOM ERRORS USING raise
# ============================================================

def withdraw(amount):
    if amount > 5000:
        raise ValueError("Withdrawal limit exceeded")
    return amount

try:
    withdraw(7000)
except ValueError as e:
    print("Custom Error:", e)

