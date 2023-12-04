# 6-4. Glossary 2:

functions = {'print': 'Outputs text or variables to the console.',
             'length': 'Returns the length of an object.',
             'type': 'Returns the type of an object.',
             'input': 'Takes user input from the console.',
             'int': 'Converts a user input an integer.'}
"""
for function, defin in functions.items():
    print(f"The {function.title()}: {defin}")  """


def glossary2(dictionary):
    while True:
        glossary = input('Enter the function or the definition (enter 0 to exit): ')

        if glossary == '0':
            break  # Exit the loop if the user enters '0'

        found_key = [key.title()
                     for key in dictionary.keys()
                     if glossary == key
                     ]
        found_value = [f"{key.title()}: {value}"
                       for key, value in dictionary.items()
                       if glossary in value
                       ]

        if found_key:
            print("Matching key:")
            print("\n".join(found_key))
        elif found_value:
            print("Matching value:")
            print("\n".join(found_value))
        else:
            print("No matches found.")


# Call the function with your dictionary
glossary2(functions)
