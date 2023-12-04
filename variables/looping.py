# list - DS, iterable object, object with multiple items(elements) in it
# For loop - looping allows you to take the same action, or set of actions, with every item in a list

cars = ['tasla','bmw','pagani','vaz','lexus']
#for_varForEachIteration in nameOfTheList
# Looped introducing of list

# if you have 4 items in the list, for loop iterates 4 times, code in for loop is repeated 4 times.
for car in cars:
    print(f"I Like my {car.title()}.") # This line is part of for loop block

# 'pass' do nothing
# scope of the 'guest' variable is within for block(inside the loop)
# nested for loop
# H/W 4-1,4-2

print("_________H/W__________")

pizzas = ['paperoni','cheeses','carbonara','bq']
for pizza in pizzas:
    print(f"I like {pizza.title()}")
print("I love different pizzas")
# list[str] = ['dog','cat','duck','squirrel']
# Animals
print("______________")
animals = ['dog','cat','duck','squirrel']
for animal in animals[2:4]:
    print(f"We feed the {animal} bread")

for animal in animals[0:2]:
    print(f"A {animal} would make a great pet")

# Example 2
animals = ['dog','cat','duck','squirrel']
# Print sentences for animals at index 2 and 3
print("\n".join(f"We feed the {animal} bread" for animal in animals[2:4]))

# Print sentences for animals at index 0 and 2
print("\n".join(f"A {animal} would make a great pet" for animal in animals[0:2]))
print("I love all these animals")
# "\n" represents a newline character.
# separator.join(iterable)
# Example:
# my_list = ["apple", "orange", "banana"]
# result = ", ".join(my_list)
    # Output:
    # apple, orange, banana


guests = ['rikky','sony','angelo','anton']
# Looping using index
# find how many elements in the list? len(guests)
# loop number of times as number of elements
print('length: ', len(guests))
for i in range(len(guests)): # range(4) 0, 1, 2, 3
    print(f"current index :{i}")
    del guests[0]  # removing elements by index
print(f"\n{guests}")




