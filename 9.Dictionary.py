students = {
    "uniName" : "Kohsar University Murree",
    "departments" : ["Computer Science","Software Engineering"],
    "teachers" : ("PHD","MSC"),
    "total_students": 333
}

print (students)
print(students["teachers"])
print (type(students))

#Nested Dictionaries
faculty = {
    "name" : "Computer Science",
    "computer_sciece" :{
        "name":"Asim Khan",
        "batch": "2025",
    }
}

print(faculty)
print(faculty["computer_sciece"])
print(faculty["computer_sciece"]["batch"])

#Dictionary Methods


#Keys Method:It will give all of the key values
print(faculty.keys())

#Values: It will return the values
print(faculty.values())





print(len(faculty))