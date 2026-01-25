# in python function are treated as FIRST CLASS CITIZENS 
# A function can take one or more functions as parameters
# A function can be returned as a result of another function
# A function can be modified
# A function can be assigned to a variable


def sum_numbers(nums):
    return sum(nums)  # built in sum func

def hof(fn,numbers):    # takes functions as parametre
    res=fn(numbers)
    return res

print(hof(sum_numbers,[1,2,3,4]))


def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add      # returning function

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20