# If we are interested in an index of a list, we use enumerate built-in function to get the index of each item in the list.

nums=[5,6,4,7,2]
for idx,item in enumerate(nums,start=1):
    print(idx,item)


countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')