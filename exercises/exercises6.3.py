# 6-4. Glossary 2:

functions = {'print': 'Outputs text or variables to the console.',
             'length': 'Returns the length of an object.',
             'type': 'Returns the type of an object.',
             'input': 'Takes user input from the console.',
             'int': 'Converts a user input an integer.'}

while True:
    glossary = input('Enter the function or the definition (enter 0 to exit): ')

    if glossary == '0':
        break  # Exit the loop if the user enters '0'
# We assign key to glossary
    found_key = [key.title()
                 for key in functions.keys()
                 if glossary in key
                 ]
# We assign value to glossary
    found_value = [f"{key.title()}: {value}"
                   for key, value in functions.items()
                   if glossary in value
                   ]
# if glossary match to key
    if found_key:
        print("Matching key:")
        print("\n".join(found_key))
# if glossary match to value
    elif found_value:
        print("Matching value:")
        print("\n".join(found_value))
    else:
        print("No matches found.")
