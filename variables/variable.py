# Variable - storage for values, with can be reused by var name
import math
message = "I am variable value and can be changed."
print(message)
print('Second time using the message value: ' + message)
num1 = 25
num2 = 30.45
status = True

print("Data type of the message variable", type(message))
print("Data type of the num1 variable", type(num1))
print("Data type of the num2 variable", type(num2))
print("Data type of the status variable", type(status))

print("Value of the num1 variable: " + str(num1)) # here str() function converts int to string
print("Value of the num1 variable:", num1) # here print() function convert int to string
print("Value of the num2 variable:", num2)
print("Value of the status variable:", status)

# fstring - format+string
print(f"Value of the num1 variable: '{num1+50}'.")
print(f"Value of the num1 variable: '{num1*50}'.")

num3 = f"num1 multiplied by 50: {num1+50}"
num4 = "Value of the num1 variable:", num1
print(num3)
print(num4)
# This functions: title(), upper(), lower() for string variables
print(message)
print(message.title())
print(message.upper())
print(message.lower())

msg = '    python '
print(msg.strip())
comment_string = '#.....>< )( section 3.2.1. Issue @32  .  ..  ... .'
print(comment_string)
print(comment_string.strip('.#!>123 '))

num5 = '25'
print(int(num5)+10)

# Mathematical operations +, -, *, /
# in Python: // (floor division), % (modulo)
print(f"Addition of numbers: {num1 + num2}")
print(f"Division of numbers: {round(num1/num2, 4)}")

num1 = 22
num2 = 4
print(f"Numbers we have: num1 = {num1} and num2 = {num2}")
print(f"Division of numbers: {num1 / num2}")
print("****** # in Python: // (floor division), % (modulo) *******")
print(f"Floor division of numbers: {math.floor(num1 / num2)}")
print(f"Modulo division of numbers: {num1 % num2}")

# Data types: number, text, boolean

# code to swap a and b value
a = 10
b = 50
print(a,b)
c = b
b = a
a = c
print(a,b)

# Or to swap volue

x=60
y=100
print(x,y)
x,y=y,x
print(x,y)