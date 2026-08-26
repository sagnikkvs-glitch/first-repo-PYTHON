# 1. File Handling

# File handling is used to create, read, write and
# modify files using Python.
#
# Common modes:
# "r" -> Read
# "w" -> Write
# "a" -> Append


# 2. Opening a File

# open() is used to open a file.
#
# Syntax:
# open("filename", "mode")

file = open("example.txt", "r")
file.close()


# 3. Reading a File

# read() is used to read the entire content of a file.

file = open("example.txt", "r")

content = file.read()
print(content)

file.close()


# 4. Reading Line by Line

# readline() reads one line at a time.

file = open("example.txt", "r")

line = file.readline()

while line:
    print(line, end="")
    line = file.readline()

file.close()


# 5. Writing to a File

# "w" mode is used to write data to a file.
# If the file already contains data, "w" will replace it.

file = open("example.txt", "w")

file.write("Hello, Python!\n")
file.write("I am learning File Handling.")

file.close()


# 6. Appending to a File

# "a" mode is used to add new data at the end
# of an existing file.
# It does not delete the existing content.

file = open("example.txt", "a")

file.write("\nThis is a new line.")

file.close()