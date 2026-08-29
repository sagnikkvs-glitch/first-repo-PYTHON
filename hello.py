import os 
print("=== Science Notes ===")
with open ("science-notes.txt") as f:
    for line in f :
        print(line.strip())

print("\n=== Word count ===")
with open ("maths-notes.txt") as f :
    for line in f :
        print(len(line.split()), "words ->" , line.strip())

print("\n merging notes ===")
with open ("all-notes.txt", "w") as out :
    for file in["science-notes.txt", "maths-notes.txt"] :
        with open (file) as f :
            out.write(f"--- {file} ---\n{f.read()}\n" )

print("saved to all-notes.txt")

if os.path.exists("all-notes.txt") :
    os.remove("all-notes.txt")
    print("all-notes.txt deleted. ")