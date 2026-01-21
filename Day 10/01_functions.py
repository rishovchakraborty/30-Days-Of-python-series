def add_two_numbers ():   #definition
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()   # calling a function


#returning a value
def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())



# with parametres
def greet(name):
    message=f"hi {name}, welcome to python"
    return message

print(greet('Rishov'))


def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total

print(sum_of_numbers(10))


#two para
def age(current_year, birth_year):
    age=current_year-birth_year
    return str(age) + ' Y'

print(age(2026,2004))

# Key and Value 
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'rishov', lastname = 'chakraborty')
print_fullname(lastname = 'chakraborty', firstname = 'rishov')
# same result in both cases

# Default Parameters 

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' 
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - average gravity on Earth's surface
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # gravity on the surface of the Moon


