# Python Basics: Part I
## Markdown Language examples

## title 3

### title 4

### Topics covered in this project:
- Variables
- data structure
- Loops
- Conditional statements
- Object-oriented Programming concepts
    - subclass

### Start this project as follows
1. [Variables](#variables)
2. [Working with lists](/lists)
3. [Working with dictionaries](/dictionary/dictionary_intro.py)
4. Working with CRUD operations
5. Looping through dictionaries 

### More examples:
In this part of the book/project we will be learning the **basics
of Python** and how to do the problem solving.

*This text isi n Italics*

**This text is in Bolt**

### Saving the clickable link
If you want register [click here](https://www.thelevelupsolutions.com/signup)

### Embedding the picture into your text
Here is the picture of [Cat](./R.jpg)

---

picture from the website
![Cat](https://th.bing.com/th/id/OIP.VEhlSj01_sNxUEFpGYIPMwHaII?rs=1&pid=ImgDetMain)

---
### Including the code snippets in your documentation

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
```
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
    priv.add_privileges('nothing')
    priv.add_privileges('nothing')
    priv.add_privileges('nothing')
    priv.add_privileges('nothing')


Regular paragraph content
```shell
# some command line code that does not need any color coding
  # creating the reports folder under Documents
  mkdir ~/Documents/reports```