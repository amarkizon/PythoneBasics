class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed



dog = Dog("Charlie", "Bulldog")
print(dog.speak())

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

circle = Circle(5)
print(circle.radius)
circle.radius = 10
print(circle.radius)
