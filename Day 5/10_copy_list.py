# python_list_copy_explained.py
# ------------------------------------------------------------
# This file explains:
# 1. How variables reference objects in Python
# 2. Assignment vs copy
# 3. Shallow copy in lists
# 4. Deep copy in lists
# 5. Common mistakes and outputs
# ------------------------------------------------------------

# ============================================================
# 1. VARIABLES ARE REFERENCES (NOT STORAGE BOXES)
# ============================================================

# Here, 'a' does NOT store the list itself.
# 'a' stores a reference (address) to a list object in memory.

a = [1, 2, 3]

# 'b = a' does NOT create a copy
b = a

# Both a and b point to the SAME list object
b.append(4)

print("Assignment (b = a):")
print("a:", a)   # [1, 2, 3, 4]
print("b:", b)   # [1, 2, 3, 4]
print("id(a) == id(b):", id(a) == id(b))

print("\n" + "="*60 + "\n")

# ============================================================
# 2. SHALLOW COPY (OUTER OBJECT IS NEW)
# ============================================================

# copy() creates a NEW list object
# but elements inside are the SAME references

a = [1, 2, 3]
b = a.copy()

b.append(4)

print("Shallow copy with flat list:")
print("a:", a)   # [1, 2, 3]
print("b:", b)   # [1, 2, 3, 4]
print("id(a) == id(b):", id(a) == id(b))

print("\n" + "="*60 + "\n")

# ============================================================
# 3. SHALLOW COPY WITH NESTED LISTS (IMPORTANT)
# ============================================================

# Inner lists are STILL shared

a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print("Shallow copy with nested lists:")
print("a:", a)  # [[1, 2, 99], [3, 4]]
print("b:", b)  # [[1, 2, 99], [3, 4]]

# Outer list is different
print("id(a) == id(b):", id(a) == id(b))

# Inner lists are SAME
print("id(a[0]) == id(b[0]):", id(a[0]) == id(b[0]))

print("\n" + "="*60 + "\n")

# ============================================================
# 4. DEEP COPY (FULLY INDEPENDENT COPY)
# ============================================================

import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0].append(99)

print("Deep copy:")
print("a:", a)  # [[1, 2], [3, 4]]
print("b:", b)  # [[1, 2, 99], [3, 4]]

# Outer lists are different
print("id(a) == id(b):", id(a) == id(b))

# Inner lists are ALSO different
print("id(a[0]) == id(b[0]):", id(a[0]) == id(b[0]))

print("\n" + "="*60 + "\n")

# ============================================================
# 5. DIFFERENT WAYS TO DO SHALLOW COPY
# ============================================================

a = [1, 2, 3]

b1 = a.copy()
b2 = a[:]
b3 = list(a)

print("Different shallow copy methods:")
print(b1, b2, b3)

print("All different objects:")
print(id(a), id(b1), id(b2), id(b3))

print("\n" + "="*60 + "\n")

# ============================================================
# 6. COMMON MISTAKE: EXPECTING extend() TO RETURN A LIST
# ============================================================

fruits = ['banana', 'orange']
vegetables = ['tomato', 'potato']

result = fruits.extend(vegetables)

print("extend() return value:", result)  # None
print("fruits after extend:", fruits)

print("\n" + "="*60 + "\n")

# ============================================================
# 7. WHEN SHALLOW COPY IS SAFE
# ============================================================

# Immutable elements (int, float, str, tuple)

a = [(1, 2), (3, 4)]
b = a.copy()

# Safe: tuples cannot be modified
print("Shallow copy with immutable elements:")
print(a, b)

print("\n" + "="*60 + "\n")

