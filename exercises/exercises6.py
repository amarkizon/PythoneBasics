# 6-1. Person:
contact = {'first_name': 'Evgenii',
           'last_name': 'ivanov',
           'age': 35,
           'city': 'Chicago'}
print(contact['first_name'])
print(contact['last_name'])
print(contact['age'])
print(contact['city'])

# 6-2. Favorite Numbers:
friends = {'vadim': 818,
           'parvis': 929,
           'katya': 212,
           'evgenii': 872,
           'scom': 702}
print(friends)

# 6-3. Glossary:

functions = {'print': 'Outputs text or variables to the console.',
             'length': 'Returns the length of an object.',
             'type': 'Returns the type of an object.',
             'input': 'Takes user input from the console.',
             'int': 'Converts a value to an integer.'}
while functions != str(0):
    glossary = input('Enter the function: ')
    function = functions.get(glossary, 'Not found') # 'get' gives us two options for input
    # If data in 'function' it's one option if data out of 'function' it's another option
    print(f"{glossary.title()} function: {function}")