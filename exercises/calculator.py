"""# Example 1
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)

print(z)

# Example 2
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x+y)

# Example 3
print(int(input("What's x? ")) + int(input("What's y? ")))

# Example 4
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)

print(f"{z:,}")

# Example 5     """
x = float(input("What's x? "))
y = float(input("What's y? "))
"""
z = round(x / y, 2)

print(z)

score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")       """

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
main()

z = x / y

print(f"{z:.2f}")