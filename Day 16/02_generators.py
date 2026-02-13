"""Quick intro to generators and the `yield` keyword.

Instead of building a full list in memory, a generator gives you
one value at a time while it runs.
"""


def count_up_to(limit):
    """Yield numbers from 1 up to `limit` (included)."""
    current = 1
    while current <= limit:
        yield current
        current += 1


print("Using the generator with a for loop:")
for number in count_up_to(5):
    print(number)


# We can also use `next()` manually
print("\nManual iteration with next():")
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# If we called next(gen) again here, we would get StopIteration.


# Generator expression: looks like a list comprehension
# but uses round brackets instead of square ones.

gen_expr = (x * x for x in range(5))
print("\nGenerator expression values:")
for value in gen_expr:
    print(value)


def even_numbers():
    """Yield even numbers starting from 0 forever."""
    n = 0
    while True:
        yield n
        n += 2


print("\nFirst 5 even numbers from an infinite generator:")
evens = even_numbers()
for _ in range(5):
    print(next(evens))

