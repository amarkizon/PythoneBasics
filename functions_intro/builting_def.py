# def names of the functions
def hello():
    print(f"Hello world function!")

def hello_name(name):
    print(f"Hello World {name.title()}!")
    print(f"Thank you for joining")

def hello_return():
    msg = f"Hello world function!"
    msg1 = f"second line"
    msg2 = "third line"
    msg3 = "*********************"
    final_msg = f"{msg}\n{msg1}\n{msg2}\n{msg3}"
    return final_msg

def addition(num1, num2):
    # print(f"Addition: {num1} + {num2} = {num1 + num2}")
    if (type(num1) == float) or (type(num2) == float):
        result = sum(num1 + num2)
    if num1 is None or num2 is None:
        result = 'Error'
    else:
        result = 'Error'
    return result

def calculate_monthly_payment(balance, terms, rate):
    print("calculating the monthly rate ...")
    # Check if rate is not provided or is an empty string
    if not rate:
        rate = 5
    # Convert rate to a decimal
    rate /= 100.0
    # Check for division by zero (avoiding potential ZeroDivisionError)
    if terms == 0:
        return "Error: Terms should be greater than 0"
    # Calculate monthly interest and principal
    monthly_int = (balance / terms) * (rate / 12)
    monthly_prin = (balance / terms)
    # Calculate and return the monthly payment
    monthly_payment = monthly_prin + monthly_int
    return monthly_payment

def greet_user(names: list):
    # print a simple greeting to each user in the list.
    for name in names:
        msg = 'Hello, ' + name.title() + "!"
        print(msg)

def totaling(a: int, b: int) -> int:
    return a + b