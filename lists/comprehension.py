cars = ['toyota','lexus','honda','bmw']
nums = [2, 3, 8, 29, 19]
# create list of squares, print the list
squares = []
for num in nums:
    squares.append(num**2)
print(squares)

# List comprehension - list and append in one line
cubes = [num**3 for num in nums]
print(cubes)

updated_cars = [car for car in cars]
updated_cars = [car.upper() for car in cars[:3]]

print(updated_cars)
print(cars)
print(f"last car in the list {cars[-1]}.")