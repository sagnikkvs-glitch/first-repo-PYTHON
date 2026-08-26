n=int(input("how many charcters to preview: "))
file= open("class-notes.txt", "r")
print(file.read(n))
print()

file = open("class-notes.txt", "r")
lines =  file.readlines()
file.close()

print("total lines:", len(lines))
for i in range(len(lines)):
    print( i+1 , "->", lines[i].strip())
print()

word = input("skip lines starting with: ")
file = open("class-notes.txt","r")
for line in file:
    if line.startswith(word):
        print("skip ->", line.strip())
    else:
        print("keep ->", line.strip())
file.close()
print()

file= open("class-notes.txt", "r")
lines =  file.readlines()
file.close()
out = open("odd-lines.txt", "w")
for i in range(0, len(lines),2):
    out.write(lines[1])
out.close()
print("odd lines saved th odd-lines.txt")