class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""

        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""

        print(self.name.title() + " rolled over!")


class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is " + self.name)  # this is java


# First Robot
r1 = Robot('Tom', 'red', 30)
# Second Robot
r2 = Robot('Jerry', 'blue', 40)

r1.introduce_self()
r2.introduce_self()


# 9-1. Restaurant:
class Restaurant:
    # Assuming 'opened' is a variable indicating an open condition
    def __init__(self, restaurant_name, cuisine_type, condition, number_served):
        """ Initialize place and type attributes """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.condition = condition
        self.number_served = number_served

    def describe_restaurant(self):
        """ Prints info about the restaurant """
        print(f"The {self.restaurant_name} restaurant has a {self.cuisine_type} cuisine")

    def open_restaurant(self):
        """ Determines if the restaurant is open """
        if self.condition == 'opened':
            print(f"The {self.restaurant_name} is opened.")
        elif self.condition == 'closed':
            print(f"The {self.restaurant_name} is closed.")
        else:
            print(f"The {self.restaurant_name} is closed.")

    # 9-4. Number Served:
    def reserved_table(self):
        """Print a statement showing the served number."""
        if self.number_served != str():
            print("Table has not reserved")
        else:
            print("Reserved number is " + str(self.number_served))


# First restaurant:
res1 = Restaurant('dominnos', 'italian', 'opened', 68)

# Execution:
res1.describe_restaurant()
res1.open_restaurant()
res1.reserved_table()

# 9-5. Number Served:

class User:
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.login_attempts = 0

    def increment_attempts(self):
        print("Incrementing the login attempts ...")
        # self.login_attempts = self.login_attempts + 1
        self.login_attempts += 1
        print('attempts:', self.login_attempts)

    def reset_attempts(self):
        print("Resetting the login attempts ...")
        self.login_attempts = 0
        print('attempts:', self.login_attempts)

    def describe_user(self):
        print(f"The summary of info: {self.first_name.title()}, {self.last_name.title()}, {self.email},"
              f"{self.password}, {self.login_attempts}")

    def called_great_user(self):
        print(f"Welcome, {self.first_name.title()} {self.last_name.title()}")

class Admin(User):
    """ Exercise 9-7 """
    def __init__(self, first_name, last_name, email, password):
        upper().__init__(first_name, last_name, email, password)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)

user1 = User('anton', 'ivanov', 'ash.rest@gmail.com', '1234562566')
user1.increment_attempts()
user1.increment_attempts()
user1.increment_attempts()
user1.reset_attempts()