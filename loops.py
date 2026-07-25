# for loop
# range(start_val, end_val+1, step_size)
for i in range(0, 11, 3):
    print(i)

for i in range(0, 11):
    print(i)


# nested loops:->this means a loop inside another loop
for i in range(1, 4):
    for j in range(5, 8):
        print(i, j)

# an eg with words
adj = ["red", "healthy", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)


#  while loop:-> means that the loop will continue to run as long as the condition is true

i=3
while i<10:
    print(i)
    i += 1