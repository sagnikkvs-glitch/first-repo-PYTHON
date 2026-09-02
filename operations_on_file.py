# 1. read()

# read() is used to read the entire content of a file.

file = open("example.txt", "r")

content = file.read()
print(content)

file.close()


# 2. readlines()

# readlines() reads all the lines of a file
# and stores them in a list.

file = open("example.txt", "r")

lines = file.readlines()
print(lines)

file.close()


# 3. Looping Through a File Line by Line

# We can use a for loop to read and print
# each line one by one.

file = open("example.txt", "r")

for line in file:
    print(line, end="")

file.close()


# 4. Filtering Lines with Conditions

# We can use conditions to select only the
# lines that match a particular requirement.

file = open("example.txt", "r")

for line in file:
    if "Python" in line:
        print(line, end="")

file.close()


# 5. Copying Selected Lines to a New File

# We can read lines from one file and write
# only the selected lines into another file.

source = open("example.txt", "r")
destination = open("selected.txt", "w")

for line in source:
    if "Python" in line:
        destination.write(line)

source.close()
destination.close()