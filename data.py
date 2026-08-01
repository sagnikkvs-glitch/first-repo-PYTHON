#lists
students = ["arav", "priya", "sneha","dev"]
print(students)

students.append("meera")
students.remove("dev")
print(students)

# dictionary

teacher = {"name": "MR.sharma", "subject":"python"}
teacher["email"]= "sharma@school.com"
print("teacher")

# student dictionary
directory = dict(zip([1,2,3,4,5] ,  students))
print(directory)
print(directory[3])

