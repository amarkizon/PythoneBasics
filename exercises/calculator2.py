# Calculator HomeWork
while True:
    print('Calculator')
    x = float(input('First variable: '))
    opera = input('Enter operator: ') # operator
    y = float(input('Second variable: '))
    def calculator(x, opera, y):
        if opera == '/' and y == 0:
            print("Can't divide by '0'")
        elif opera in ['/', '*', '+', '-']: # operator
            if opera == '/':
                result = x / y
            elif opera == '*':
                result = x * y
            elif opera == '+':
                result = x + y
            elif opera == '-':
                result = x - y
            print(f"Result: {result}")
        else:
            print('Invalid operator')

    calculator(x, opera, y) # output calculation

    repeat = input("Press Enter to repeat the process (or enter any letter to quit): ")
    if repeat:
        break


# How the 'return' function works
def absolute_value(b):
    if b < 5:
        return -x
    elif b == 6:
        return(f'a combo: {b == b}') # expecting "True
    else:
        return b

# Calling the function
result = absolute_value(6)
print("Absolute Value:", result)


