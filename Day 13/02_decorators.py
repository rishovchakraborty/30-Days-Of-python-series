# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. Decorators are usually called before the definition of a function you want to decorate.

#   normal function
def greeting():
    return 'hi hellow ! Rishov'

def upper_case(func):
    def wrapper():
        fun=func()
        return fun.upper()
    return wrapper

g=upper_case(greeting)
print(g)
print(g())  # HI HELLOW ! RISHOV


## Let us implement the example above with a decorator

def upper_case(func):
    def wrapper():
        fun=func()
        return fun.upper()
    return wrapper

@upper_case
def greeting():
    return 'hi hellow ! Rishov'

print(greeting()) # HI HELLOW ! RISHOV

