Write a Python program demonstrating polymorphism by creating a base class Shape with a method
area(), and two subclasses Circle and Rectangle that override the area() method. Instantiate objects
of both subclasses and call the area() method. Explain how polymorphism simplifies working with
different shapes in an inheritance hierarchy

import math

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print("Area:", shape.area())
