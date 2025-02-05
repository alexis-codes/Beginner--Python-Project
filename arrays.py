courses = ["MIT", "Cybersecurity", "Datascience"]
print(courses)


#Accessing an element
print(courses[2])

#Looping through an array
for x in courses:
    print("Course is", x)


#Adding a new elements into an array
courses.append("Laravel")
print(courses)


#Remoivng an element from an array
courses.remove("Cybersecurity")
print(courses)