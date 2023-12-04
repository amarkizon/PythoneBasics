# - comment line

# echo in Linux, print in python, it prints the text in STDOUT
# print is the function in python (method)
# Run - Shift, f10

# Example 1
"""
name = input("what's your name? ")
print("Hello, ", end="")
print(name)

# Example 2

name = input("what's your name? ")
print("Hello, ", name, sep='')

# Example 3

print("Hello, 'Friend'")
print("Hello, \"Friend\"")

# Example 4

print(f"Hello, {name}")
                                """
# Example 5

# Ask user for their name \/        \/ Remove whitespace from str and capitalize user's name
name = input("what's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")
# Say hello to user
print(f"Hello, {first}")

"""
Possible errors you might face when you coding:
SyntaxError: when your code is written wrong, like: ",()
NameError: when you type incorrect function name, string is not closed, not covered with quote ""
python is sensitive for the spaces in the beginning of the line
Indentations a space error
"""
