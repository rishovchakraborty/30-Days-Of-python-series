# A function that remembers variables from its enclosing scope, even after the outer function has finished executing

def outer():
    x=10
    def inner():
        print(x)
    return inner

f=outer()
# f()
print(f.__closure__)

# outer() finishes execution

# x should be destroyed

# BUT inner() remembers x

# That memory is a closure