# 1. Inheritance

# Inheritance allows a child class to use the
# properties and methods of a parent class.

class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()
dog.eat()
dog.bark()


# 2. Parent Class and Child Class

# Parent class: The class whose properties and methods
# are inherited.
# Child class: The class that inherits from the parent class.

# Animal = Parent class
# Dog = Child class


# 3. Calling the Parent Constructor

# A constructor is the __init__() method.
# super().__init__() is used to call the parent constructor.

class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll


student = Student("Sagnik", 10)

print(student.name)
print(student.roll)


# 4. super()

# super() is used to access methods or the constructor
# of the parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog barks")


dog = Dog()
dog.sound()


# 5. Abstraction

# Abstraction means hiding unnecessary details
# and showing only the important information.
# Python uses ABC and @abstractmethod for abstraction.


# 6. Abstract Methods with @abstractmethod

# @abstractmethod is used to create an abstract method.
# A child class must implement the abstract method.

from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Area =", self.length * self.width)


rectangle = Rectangle(10, 5)
rectangle.area()