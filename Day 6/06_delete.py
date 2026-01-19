fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits[0]  # 'tuple' object doesn't support item deletion
print(fruits)
del fruits      # it is possible to delete the tuple itself using del.
print(fruits)