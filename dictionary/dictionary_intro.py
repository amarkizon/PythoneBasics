# data structure: Dictionary
# element consist of key and value pair
# key is unique

# CRUD
print("******** Creating the dictionary ********")
customers = {'customerID': 101,
             'customerName': 'level up cgi',
             'country': 'USA',
             'city': None}
student = {}
teacher = dict()
print("****** Read/access to elements ******")
print(customers)
print(customers['customerName'])
print(customers['customerID'])
print(customers['country'])
print(list(customers.keys()))

print('***** Updating the elements *****')
customers['customerName'] = 'Level Up Academy'
customers['customerID'] = 102
print(customers)

print('***** Deleting the elements *****')
del customers['country']
customers.pop('city')
print(customers)

print('***** Adding the elements *****')
customers['city'] = 'Brooklyn'
print(customers)


print(f"{customers['customerName']}company is located in {customers['city']}")
print('=================')

customer1 = {'customerID': 101,
             'customerName': 'Level Up Group',
             'country': 'USA',
             'city': 'Brooklyn'}
customer2 = {'customerID': 102,
             'customerName': 'Universal Bank',
             'country': 'USA',
             'city': 'Manhattan'}
customer3 = {'customerID': 103,
             'customerName': 'First Bank',
             'country': 'USA',
             'city': 'Columbia DC'}

customers = [customer1,
             customer2,
             customer3]
print(customers)
for key in customer1.keys(): # This loop through keys only
    print(f"key: {key}")
    print(customer1[key]) # print the value
    print(customer1[key]) # print the value

for value in customer1.items():
    print(f"value option1: {customer1[key]}") # prints the value of given key in each iteration
    print(f"value - option2: {value}") # print the value in each iteration
print(customer3['city'],',', customer3['country'])



# H/W 6-1, 6-2, 6-3

# H/W 6-4, 6-5, 6-6

