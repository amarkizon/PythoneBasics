def hello():
    msg = f"Hello World function!"
    msg1 = f"Second line"
    msg2 = f"third line"
    msg3 = f"fifth line"
    msg4 = f"********************"
    final_msg = f"{msg}\n{msg1}\n{msg2}\n{msg3}\n{msg4}\n"
    print(final_msg)

# 2. execute the function:
hello() # executing lines in the hello() function

result_of_print = hello() # executes the line in the function, but does not return a value
print(hello())
# print(result_of_print)
print("-------------------------")

def calculate_monthly_payment(balance, terms, rate):
    print("calculating the monthly rate ...")
    monthly_int = (balance / terms) * (rate/12)
    monthly_prin = (balance / terms)
    monthly_payment = monthly_prin + monthly_int
    return monthly_payment

payment_with_extra = calculate_monthly_payment(10000, 60, 5) + 100
print(f"calculate_monthly_payment: {calculate_monthly_payment(10000, 60, 5)}")
print("monthly payment with extra payment", payment_with_extra)

msg = ''
while msg != "no":
    loan = int(input('enter the balance in numbers only: '))
    terms = int(input('enter the terms in numbers only: '))
    rate = float(input('enter the rate in numbers only: '))
    print(calculate_monthly_payment(loan, terms, rate))
    msg = input("Do you want to continue? yes/no")

def greet_user(names: list):
    # print a simple greeting to each user in the list.
    for name in names:
        msg = 'Hello, ' + name.title() + "!"
        print(msg)

def totaling(a: int, b: int) -> int:
    return a + b