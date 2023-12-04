countries = ['usa','canada','france','uk']
nums = []
if nums:
    print("List is not empty")
else:
    print("List is empty")

for country in countries:
    if country == 'usa'.lower(): # make the variable lower case to compare with lower case 'usa'
        # following line is executed when country == 'usa' expression returns True
        print(country.upper())
    else:
        # ia all other cases
        print(country.title())

# Expression you can use in if statement
# False: 0, empty list, empty dictionary
# a == b
# a >= b : num >= 456, num <= 456
# a != b : num ! = 0
# a > b : num > 22, num < 22
# else in list : 'usa' in countries, 34 in nums

# combination of conditions using operator : OR, AND
# a == b or a == c : either a is equal to b or a is equal to s
# True or True == True
# True or False == True
# False or False == False

# a == b and a == c : a is equal to b and c
# a == b and b == c: a is equal to b and c
# True and True == True
# True and False == False
# False and False == False

b = 20
a = 10
print(a == b) # comparing the value of 'a' variable to value of 'b' variable

age = 18
if age < 17:
    print(f" You are not eligible, but you can apply for driving licence after {17 - age} years")
elif 17 < age < 25:
    print(f"You are eligible to apply for DL for junior")
else:
    print("You can eligible to apply for driving licence.")

print("================================================")
nums = [45, 4, 566,88, 1, 0]
# print i found it when 88 in the list
num = input("enter the number to check: ")
print("Number from the input:", num)
num = int(num)
print(type(num))
if num in nums:
    print("I found it")
else:
    print("Num does not exist")

# Ctrl + Shift moves lines up and down

# H/W 5-3, 5-5, to 5-11
# FuzzBuzz :
# pass a number as input. convert to int
# if num dividable by 3 print Fuzz
# if num dividable by 5 print Buzz
# if num dividable by 3 and 5 print FuzzBuzz