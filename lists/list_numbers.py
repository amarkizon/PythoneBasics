# Making Numerical list

for i in range(4, 10):
    print(f"number in this iteration: {i}")

print('data type of range function result: ', type(range(10)))
print('****** Creating the list from the range() result: ******')

nums1 = list(range(10))
print(f"nums1 list: {nums1}")

# Problem 1: print the squares of even numbers from 100 to 120 (inclusively)

for num in range(100,121,2):
    print(num ** 2)

print('OR') # Or

squares = []
for num1 in range(100, 121, 2):
    squares.append(num1 * num1)
print(f'Final list: {squares}')

print('************ MULTIPLICATION TABLE *****************')
for i in range(1, 11):
    print()  # This wraps to a new line when 'i' changes
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}', end='\t\t')
# '\t' means 'Tab'

print("****** find the max and min in the list. ******")
nums = [5, 0, 2, 25]
nums.sort() # sorts in ascending (lowest to highest)
min_num = nums[0]
max_num = nums[-1]
print("*** find the sum of list elements. ***")
# pseudocode
# have new variable for sum=0
print(nums)
total = 0
# Loop through the list then keep incrementing the sum by each element: sum = sum + num
for num in nums:
    total = total + num
    print(f"current sum: {total}")
    print(f"current num: {num}")
# after loop print the result
print(f"SUM:{total}")

# Working with partial list
print("_________________________!!!")

players = ['charles','martina','michael','florence','eli']
print(f"players[1:3]: {players[1:3]}")
print(f"players[:4]: {players[:4]}")
print(f"players[3:]: {players[3:]}")
print(f"players[:]: {players[:]}")

duplicate_players = players
copy_players = players[:]
print("*********** Original lists *************")
print(f"players: {players}")
print(f"duplicate_players: {duplicate_players}")
print(f"copy_players: {copy_players}")
print("*********** Adding new elements to each list *************")
players.append('alex')
duplicate_players.append('john')
copy_players.append('jane')
print("*********** Updated list *************")
print(f"players: {players}")
print(f"duplicate_players: {duplicate_players}")
print(f"copy_players: {copy_players}")
print("**** Looping through part of the list: ****")
for players in players[1:3]:
    print(f"players: {players}")




# H/W 4-10,4-11,4-12

print("\n\n")
players = ['charles','martina','michael','florence','eli','jane','rikko']
print(f"The first three items in the list are: {players[0:3]}")
print(f"Three items from the middle of the list: {players[2:5]}")
print(f"the last three items in the list: {players[4:7]}")


pizzas = ['paperoni','cheeses','carbonara','bq']
friend_pizzas = pizzas[:]
print(friend_pizzas)
pizzas.append('mocha')
friend_pizzas.append('asparagus')
# Iterate over both lists simultaneously using zip
for my, fr in zip(pizzas[:9], friend_pizzas[:9]):
    # Format the output to display in two columns
    print(f"My favorite pizzas are: {my.ljust(22)} My friend’s favorite pizzas are: {fr}")

# polymorphism concept - a. using the function in multiple ways, OOP concepts
