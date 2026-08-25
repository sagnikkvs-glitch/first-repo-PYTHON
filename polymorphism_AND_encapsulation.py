# 1. Polymorphism

# Polymorphism means "many forms".
# The same method or function can behave differently
# depending on the object.

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


dog = Dog()
cat = Cat()

dog.sound()
cat.sound()


# 2. Method Overriding

# Method overriding happens when a child class
# provides its own version of a method already
# present in the parent class.

class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


dog = Dog()
dog.sound()


# 3. Polymorphism with a Loop

# A loop can be used to call the same method
# on different objects.

class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()


# 4. Encapsulation

# Encapsulation means keeping data and methods
# together inside a class and controlling access
# to the data.

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount(5000)
account.show_balance()


# 5. Private Attributes with __

# An attribute beginning with __ is treated as a
# private attribute.
# It should not be accessed directly from outside
# the class.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def show_marks(self):
        print("Marks:", self.__marks)


student = Student(95)
student.show_marks()


# 6. Setter Methods

# A setter method is used to change the value
# of a private attribute safely.

class Student:
    def __init__(self, marks):
        self.__marks = marks

    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            print("Invalid marks")

    def show_marks(self):
        print("Marks:", self.__marks)


student = Student(80)

student.show_marks()

student.set_marks(95)

student.show_marks()