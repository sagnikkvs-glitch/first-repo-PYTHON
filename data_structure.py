# List  -  ordered, can be changed
scores = [85, 90, 78, 95]

# Dictionary  -  labelled key-value pairs
student = {"name": "Aarav", "age": 13}

# Tuple  -  ordered and fixed (cannot be changed)
coordinates = (10, 20)

# Set  -  unique items only, no duplicates
colours = {"red", "blue", "green"}

# In this lesson we focus on Lists and Dictionaries

# Creating a list
fruits = ["apple", "mango", "banana", "grapes", "orange"]

# Accessing items by index (starts at 0)
print(fruits[0])     # apple
print(fruits[-1])    # orange  (last item, use -1)

# Finding the total number of items
print(len(fruits))   # 5

# Slicing - getting a range of items,, here start from 1 but end before 3
print(fruits[1:3])   # ['mango', 'banana']

#  List Operations — Modifying and Organising

fruits = ["apple", "mango", "banana", "grapes"]

fruits.append("orange")   # Add to end
# ['apple', 'mango', 'banana', 'grapes', 'orange']

fruits.remove("mango")    # Remove by value
# ['apple', 'banana', 'grapes', 'orange']

fruits.pop(1)             # Remove by index  (removes 'banana')
# ['apple', 'grapes', 'orange']

fruits.sort()             # Sort alphabetically
# ['apple', 'grapes', 'orange']

fruits.reverse()          # Reverse the order
# ['orange', 'grapes', 'apple']

fruits.clear()            # Remove all items
# []


# Dictionaries — Storing Data with Labels
# A dictionary in Python stores data as key-value pairs. Each key is a unique label, and each value is the information attached to that key. Dictionaries are written using curly braces { }, with a colon : separating each key from its value. Keys must be unique, but values can repeat.

# Creating a dictionary
student = {"name": "Aarav", "age": 13, "grade": 7}

# Accessing values by key
print(student["name"])    # Aarav
print(student["age"])     # 13

# Printing the full dictionary
print(student)
# {'name': 'Aarav', 'age': 13, 'grade': 7}


# Dictionary Operations — Access, Update and Remove
# After a dictionary is created, Python provides methods to read values safely, update existing values, add new key-value pairs, remove specific entries, and clear all data. 

student = {"name": "Aarav", "age": 13, "grade": 7}

# Safe access using .get()  -  no error if key is missing
print(student.get("age"))               # 13
print(student.get("school", "N/A"))     # N/A

# Update an existing value
student["age"] = 14

# Add a new key-value pair
student["school"] = "Sunrise Academy"
print(student)
# {'name': 'Aarav', 'age': 14, 'grade': 7, 'school': 'Sunrise Academy'}

# Remove a specific key
student.pop("grade")
print(student)
# {'name': 'Aarav', 'age': 14, 'school': 'Sunrise Academy'}

# Clear the entire dictionary
student.clear()
print(student)   # {}


# 6. Converting a List into a Dictionary

# WHAT IT IS

# Python lets you pair two related lists together and convert them into a dictionary using the zip() function and the dict() constructor. This is useful when you have a list of keys (like roll numbers) and a separate list of values (like student names) and want to link them together as key-value pairs.


# Two related lists
roll_numbers = [1, 2, 3, 4, 5]
names = ["Aarav", "Priya", "Rahul", "Sneha", "Dev"]

# Convert to a dictionary using zip()
students = dict(zip(roll_numbers, names))
print(students)
# {1: 'Aarav', 2: 'Priya', 3: 'Rahul', 4: 'Sneha', 5: 'Dev'}

# Look up a student by roll number
print(students[3])   # Rahul
