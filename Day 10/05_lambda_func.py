# A lambda function is a small anonymous function (a function without a name).

# lambda arguments : expression
# 🔹 No return keyword
# 🔹 Expression result is automatically returned
# 🔹 Only ONE expression allowed


is_even= lambda x: x%2==0
print(is_even(4))

square = lambda x: x * x
print(square(5))


max_num = lambda a, b, c: a if a > b and a > c else b if b > c else c
print(max_num(3, 7, 5))


greet = lambda: "Hello World"
print(greet())



# Lambda can form a closure.
def multiplier(n):
    return lambda x: x * n

double = multiplier(2)
triple = multiplier(3)

print(double(5))   # 10
print(triple(5))   # 15
