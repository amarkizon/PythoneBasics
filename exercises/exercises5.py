import math
# 5-3. Alien Game
"""
print("XXX=== Alien Game ===XXX")
# alien_color: green, yellow, red
alien_colors = ['green', 'yellow', 'red']
points = 0

for i in range(4):
    alien_color = input("enter the color: ")
    if alien_color.lower() in alien_colors:
        print("You earned 5 points")
        points += 5 # points = points + 5
        print(f'Your total points: {points}')
    else:
        print("Sorry, no points granted.")
        print(f'Your total points: {points}')       """

# 5-5. Alien Colors #3:
# alien_color: green, yellow, red
points = 0
"""
for i in range(4):
    alien_color = input("enter the color: ")
    if alien_color.lower() in 'green':
        print("You earned 5 points")
        points += 5 # points = points + 5
        print(f'Your total points: {points}')
    elif alien_color.lower() in 'yellow':
        print("You earned 10 points")
        points += 10 # points = points + 10
        print(f'Your total points: {points}')
    elif alien_color.lower() in 'red':
        print("You earned 10 points")
        points += 15  # points = points + 15
        print(f'Your total points: {points}')
    else:
        print("Sorry, no points granted.")
        print(f'Your total points: {points}')
                                                    """
# 5-6. Stages of Life:
"""
age = int(input("Enter the person's age: "))
if age <= 2:
    print('The person is a baby.')
elif 2 < age <= 4:
    print('The person is a toddler.')
elif 4 < age <= 13:
    print('The person is a kid.')
elif 13 < age <= 20:
    print('The person is a teenager.')
elif 20 < age <= 65:
    print('The person is an adult.')
else:
    print('The person is an elder.')
                                            """
# 5-7. Favorite Fruit:
"""
print('My favorite fruits: apple, cherry, grape, garnet, strawberrie')
fruits = input('enter your fruit: ')
if fruits == ('cherry'.lower or 'strawberrie' or 'grape'):
    print("Berries are great for snacking")
elif fruits == ('apple' or 'strawberrie'):
    print("Let's make a cake")
elif fruits == ('cherry' or 'garnet'):  # bag
    print("Don't get it all dirty.")
else:
    print("It's not my favorite fruit")
                                                """
# 5-8, 5-9 Hello Admin:
""""
usernames = ['admin','john','player','comrad','bro']
print(list(usernames))
username = input("Enter your login: ")
if username in usernames:
    if username == 'admin'.lower():
        print(f"Hello {username}, please change your login")
    elif username == 'player'.lower():
        print(f"Hello {username}, are you ready to play")
    elif username == 'bro'.lower():
        print(f"What's Up {username}")
    else:
        print(f"Hello, {username}. Have a good day!")
else:
    print(f"Username '{username}' doesn't exist")
usernames.clear()
print(f"Users online: {list(usernames)}")       """

# 5-10. Checking Usernames:
"""
current_users = ['mansur','akhmal','john','tramp','alex']
new_users = ['lionel','anton','thom','mathew','Akhmal']
for user in new_users:
    if user.lower() in current_users:
        print(f'username {user} not available')
        del user
    else:
        print('you have successfully created accaunt')      

# 5-11. Ordinal Numbers:
ordinal_numbers = [1,2,3,4,5,6,7,8,9]
for number in ordinal_numbers:
    if number == 1:
        print(f'{number}st number')
    elif number == 2:
        print(f'{number}nd number')
    elif number == 3:
        print(f'{number}rd number')
    else:
        print(f'{number}th number')         """

# FuzzBuzz :
number = -100
while number < 1000000:
    for (i) in range(10):
        print(f"Test case {i+1}")
        number = int(input("Type in a number: "))
        if number == 0:
            print('Your answer incorrect')
        elif number % 3 == 0 and number % 5 == 0: # or nom % 15 == 0
            print("FuzzBuzz!")
        elif number % 5 == 0: # Example: 15 divided by 7 is 2 with a remainder of 1. Therefore, the result of 15 % 7 is 1.
            print("Buzz")
        elif number % 3 == 0:
            print("Fuzz")
        else:
            print('Your answer incorrect')
print("<<<<<===== FuzzBuzz process is end =====>>>>>")

