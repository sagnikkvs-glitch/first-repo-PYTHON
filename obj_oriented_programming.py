# Object-Oriented Programming: A method that uses Classes and Objects to make code reusable, readable, and simple.
# Class: A blueprint or template for defining something. It specifies what attributes are needed but contains no actual data.
# Object: A real-world entity created from a class blueprint that contains actual data and behaviors.

class fruit:
    print("hey! this is an example of classes and objects")

# Object Creation
ob = fruit()

# Methods
# Definition: Methods define how an object behaves.
# Location: They are simply functions written inside a class definition.
# Creation: You define them using the standard def keyword.
# The self Parameter: The first argument must always be self, which represents the specific object instance.
# Execution: You run a method by calling it through an object instance using dot notation (object_name.method_name())

class fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    # instance method
    def intro(self):
        print("hello, I am", self.name)

# Object Creation
apple = fruit('Apple', 'Red')
# Calling Function
apple.intro()


# _ Init_ Method
# They are used to assign values to object attributes at the time of object creation.
# It is automatically called every time the object is created for a class
# They are initialized by using def _init__()

class Car:
    # The __init__ method initializes the attributes
    def __init__(self, brand, year):
        self.brand = brand  # Attribute 1
        self.year = year    # Attribute 2


# Creating an object automatically triggers __init__
my_car = Car("Toyota", 2024)

print(my_car.brand)  # Output: Toyota


# data members and attributes (class variables and instance variables)

class Car:
    # The __init__ method initializes the attributes
    def __init__(self, brand, year):
        self.brand = brand  # Attribute 1
        self.year = year    # Attribute 2


# Creating an object automatically triggers __init__
my_car = Car("Toyota", 2024)

print(my_car.brand)  # Output: Toyota


