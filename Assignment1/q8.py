Write a Python program that defines a base class Vehicle with attributes make and model, and a
method display info(). Create a subclass Car that inherits from Vehicle and adds an additional attribute num doors. Instantiate both Vehicle and Car objects, call their display info() methods, and
explain how the subclass inherits and extends the functionality of the base class

Ans:
  class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Vehicle: {self.make} {self.model}")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Doors: {self.num_doors}")

v = Vehicle("Honda", "Civic")
v.display_info()

c = Car("Toyota", "Camry", 4)
c.display_info()
