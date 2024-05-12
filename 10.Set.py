#Set do not allow the duplicate values and it stores it as the one. Sets are mutable but the elements of  the set are immutable.
student = {2,3,4,5,6,6}
print(student)
print(type(student))

#Set Methods
student.add(1)
student.remove(5)

#student.clear()
student.pop()


#Union of the sets
set1 = {1,2,4}
set2 ={6,3,2}


print(set1.intersection(set2))
print(set1.union(set2))






print(student)


#WAP to count the classrooms needed for the subjects.
subjects = {"Python","java","c++","c++","javascript","c"}
print(len(subjects))
