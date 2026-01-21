# Scope defines where a variable can be accessed. 

x = 10

def show():
    print(x)

show()  # ✅ works


# 4 types of scope => 
# 1) local scope -> inside the current function
# 2) enclosing -> nested function
# 3) global scope -> at the top of the file 
# 4) built in scope -> python built-in names 
# Python searches variables in this order.


x = "global"

def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)
    inner()

outer()


# Modifying Global Variable (Bad Practice)
x = 10

def change():
    global x
    x = 20

change()
print(x)
