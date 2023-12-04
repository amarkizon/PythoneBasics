# 3 LIST OF GUESTS

guests = ['Vadim','Evgenee','Paris','Misha']
print('Persons invited to dinner:', guests)
print(f"Hello, {guests[0]} inviting you to dinner next friday")
print(f"Hello, {guests[1]} inviting you to dinner next friday")
print(f"Hello, {guests[-1]} inviting you to dinner next friday")
print(f"Hello, {guests[-2]} inviting you to dinner next friday")

# PS. in case we want to add variables me must use "string"
nums = [1,2,3]
print('example of addition:' + str(nums[1]))

# Evgenee can't make to dinner
message = 'we are inviting you to dinner next friday'
guests.pop(1)
guests.insert((0),'Mike')
guests.insert((4),'Saltan')
guests.insert(1,'Alex')
print(guests)
print('Hello,', guests[0].title(), message)
print(f"Hello, {guests[1].title()} {message}")
print('Hello,', guests[2].title(), message)
print('Hello,', guests[3].title(), message)
print('Hello,', guests[4].title(), message)

# Or
for guest in guests:
    print(f"Hello, {guest} {message}")
print('______________________')

# we don't have enough space on the table
del guests[4]
print(guests)

# 'Sort' function uses to organize the list
# permanent sorting will be done with sort()
print("################")

cars = ['tasla','bmw','pagani','vaz','lexus']
print("List of cars:", str(cars).strip('[]'))
carl = str(cars).strip('[]')
cars.sort()
print("Sorted list of cars:", carl)

# Temp sort is done with sorted()

cars.append('lamborghini')
print(f"Cars sorted temporary: {str(sorted(cars)).strip('[]')}")

# Descending list of cars

cars.sort(reverse=True)
print("Sorted list in desc order:", str(cars).strip('[]'))

# we add sort variable
cars_asc = str(sorted(cars)).strip('[]')
print(f"Sorted list: {cars_asc}")

# we add sort desc variable

cars_desc = sorted(cars, reverse=True)
print("Sorted list in desc order:", cars_desc)
# a*=20 / a=a*20

# len() -> length() in java
print(f'There are {len(cars)} cars.')

print("###############")
names = ['AI','LM','NC','DS']
print(names)
names.reverse()
print(names)

# H/W 3-8,3-9,3-10

