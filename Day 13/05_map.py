# The map() function is a built-in function that takes a function and iterable as parameters.

nums=[1,2,3,4,5]

def sq(x):
    return x**2

nums_sq=map(sq,nums)
print(list(nums_sq))
    



names = ['Rishov', 'Lidiya', 'Ermias', 'Abraham']  # iterable
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
# Iterates through names_upper_cased
# Applies .upper() to each name
# Consumes the iterator
# Converts it into a list

print(list(names_upper_cased)[0])
# names_upper_cased is already exhausted
# There are no values left
# list(names_upper_cased) → []
# print([][0])
# IndexError: list index out of range

# Iterators can be consumed only once.


# Fix 1: Store the list once (BEST PRACTICE)
names_upper_cased = list(map(lambda name: name.upper(), names))

print(names_upper_cased)
print(names_upper_cased[0])


# Fix 2: Re-create the iterator
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))

names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased)[0])
