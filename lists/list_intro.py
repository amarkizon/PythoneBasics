# Data structure - List (Array), Dictionary (HashMap), Sets, Tuples
# create, read (access the elements), update (modifying the DS), delete


# (C) List - collection of items, comma separated, covered with []
nums = [4, 2, 98, 33, 5]
print(nums)
print("Type of the variable: ", type(nums))
# Creating the empty list
city_names = []  # in java it would be cityNames {}
friends = list() # List( function
print(city_names)
print(friends)

# Accessing the elements of the List:

# nums[-1] = nums[4]
print('first element of nums list:', nums[0])
print('last element of nums list:', nums[4])
print('first element of nums list:', nums[-5])
print('last element of nums list:', nums[-1])

print("******** (U) Updating, Modifying the elements. ********")
countries = ['usa', 'uk', 'canada', 'mexico']
print(countries)
countries[1] = 'spain'
print('After the change', countries)
countries.append('italy')
print('After the append', countries)

# 'Append' adds value to the end of the list

# Tuple -> Immutable
countries.insert(0, 'france')
print('after inserting the value instead the usa to the list:', countries)

print("(D) Delete/removing the elements from the list.")

del countries[2] # the element with index 2
print('after deleting the "spain" from the list:', countries)

deleted_countries = []
delete_country1 = countries.pop() # by default 'pop' uses last index, this mean deletes last element
deleted_countries.append(delete_country1)
print('after using pop() on the list:', countries)
print('deleted country: ', delete_country1)
print('list of deleted countries:', deleted_countries)

# delete_country2 = countries.pop(1) # by default pop uses last index (-1), this means deletes last element
print('after using pop(1) on the list:', countries)
# print('deleted country: ', delete_country2)
deleted_countries.append(countries.pop(1))
# 1. countries.pop(1) -> executed removes the france, and return the france
# 2. deleted_countries.append('france')
print('list of deleted countries:', deleted_countries)

# (E) removing the elements by value
countries.append('canada')
print(countries)
countries.remove('canada') # removes the first occurrence of the value
print("Final list of countries:", countries)

# H/W: 3-4, 3-5, 3-6, 3-7 exercises