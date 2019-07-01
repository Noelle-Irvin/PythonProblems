# CHAPTER 12 CHALLENGES

# 1. Define a class called APPLE with four instance variables that represent
# four attributes of an apple.

class Apple:
    def __init__(self, c, w, co, ta):
        self.color = c
        self.weight = w
        self.country = co
        self.taste = ta

apple = Apple("green", 5.0, "USA", "tangy")
print(apple.color, apple.country, apple.weight, apple.taste)

# 2. Create a Circle class with a method called area that calculates and returns
# its area. Then create a Circle object, call area on it, and print the result.
# Use Python's pi function in the built-in math module.
import math

class Circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        return math.pi * (self.radius ** 2)

cir = Circle(2)
print(cir.area())

# 3. Create a Triangle class with a method called area that calculates and returns
# its area. Then create a Triangle object, call area on it, and print the result.

class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h

    def area(self):
        return self.base * self.height * 0.5

tri = Triangle(2, 2)
print(tri.area())

# 4. Make a Hexagon class with a method called calculate_perimeter that calculates
# and returns its perimeter. Then create a Hexagon object, call calculate_
# perimeter on it, and print the result.

class Hexagon:
    def __init__(self, l):
        self.length = l

    def calculate_perimeter(self):
        return self.length*6

hex = Hexagon(5)
print(hex.calculate_perimeter())
