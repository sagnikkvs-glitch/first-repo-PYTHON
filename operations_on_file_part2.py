# old way -- must remember to close
file = open('science-notes.txt', 'r')
for line in file:
    print(line.strip())
file.close()

# 1. with open() as f

# with open() automatically closes the file becuz with automatically closes the file
# after the work is completed.

# new way -- closes automatically
with open('science-notes.txt', 'r') as f:
    for line in f:
        print(line.strip())

# output (same both ways):
# Planets orbit the Sun
# The Moon causes tides
# Light is faster than sound
# Plants convert sunlight to food
# =----------------------------------------------------------------------------------------------------------------
# 2. split()

# split() is used to divide a string into a list
# of smaller parts.

text = "Python is easy to learn"
words = text.split()
print(words)
# next example:

with open('maths-notes.txt', 'r') as f:
    for line in f:
        words = line.split()
        print(len(words), 'words ->', line.strip())

# output:
# 4 words -> Triangles have three sides
# 3 words -> Pi is 3.14
# 5 words -> Area equals length times width
# 6 words -> Prime numbers divide only by one

# -----------------------------------------------------------------------------------------------------------------------
# 3. os.path.exists()

# os.path.exists() checks whether a file or folder exists.
# It returns True if it exists and False if it does not.

import os

# check if the merged file already exists
if os.path.exists('all-notes.txt'):
    print('all-notes.txt already exists - overwriting')
else:
    print('all-notes.txt not found - creating now')

# output (first run, file not yet created):
# all-notes.txt not found - creating now

# output (if run again after creating):
# all-notes.txt already exists - overwriting


# --------------------------------------------------------------------------------------------------------------------
# 4. os.remove()

# os.remove() is used to delete a file.

import os

# safe deletion -- check before removing
if os.path.exists('all-notes.txt'):
    os.remove('all-notes.txt')
    print('all-notes.txt deleted.')
else:
    print('all-notes.txt does not exist.')

# output (file was there):
# all-notes.txt deleted.

# output (file was not there):
# all-notes.txt does not exist.


# ============================================___________________________---------------------------------------------------

# 5. File Merge

# File merging means combining the contents of
# two or more files into a single file.

with open("file1.txt", "r") as f1:
    data1 = f1.read()

with open("file2.txt", "r") as f2:
    data2 = f2.read()

with open("merged.txt", "w") as f:
    f.write(data1)
    f.write("\n")
    f.write(data2)

print("Files merged successfully")

# another way__--

import os

# check before merging
if os.path.exists('all-notes.txt'):
    print('all-notes.txt already exists - overwriting')
else:
    print('all-notes.txt not found - creating now')

# build combined content from both files
content = ''
with open('science-notes.txt', 'r') as f:
    content += '--- science-notes.txt ---\n'
    content += f.read() + '\n'
with open('maths-notes.txt', 'r') as f:
    content += '--- maths-notes.txt ---\n'
    content += f.read() + '\n'

# write combined content to output file
with open('all-notes.txt', 'w') as out:
    out.write(content)
print('Saved to all-notes.txt')

# all-notes.txt will contain:
# --- science-notes.txt ---
# Planets orbit the Sun
# The Moon causes tides
# ...
# --- maths-notes.txt ---
# Triangles have three sides
# ...

# **********************************************************************************************************

# Try and Except

# try is used to write code that may cause an error.
# except is used to handle the error without stopping
# the whole program.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("Result:", a / b)

except ZeroDivisionError:
    print("You cannot divide by zero.")

except ValueError:
    print("Please enter numbers only.")
