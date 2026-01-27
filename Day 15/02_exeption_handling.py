# Python uses try and except to handle errors gracefully.\
# try:
#     code in this block if things go well
# except:
#     code in this block run if things go wrong


# try:
#     print(5+'5')
# except:
#     print('wrong vai') # as both arent sme datatype except hits



try:
    name=input('enter you name: ')
    year_born=input('the year you were born: ')
    print(type(year_born)) # <class 'str'>
    age=2026-year_born
    print(f"{name} is {age} years old...")
except TypeError:
    print('Type Error Occur') 
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

# output => Type Error Occur


try:
    name=input('enter you name: ')
    year_born=input('the year you were born: ')
    print(type(year_born)) # <class 'str'>
    age=2026-int(year_born)
    print(f"{name} is {age} years old...")
except TypeError:
    print('Type Error Occur') 
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')



try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2026 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')


try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - (year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e) # unsupported operand type(s) for -: 'int' and 'str'
