marks =[22.3,44.4,58.9]
marks.insert(1,33)
marks.sort()
print(marks)

print(type(marks))

#Mutable and can store any data type

student_record = ["Ali",22, "lahore"]
print(student_record)

print(student_record[2])
student_record[1] =33
print(student_record)

print(student_record[0:2])
print(student_record[-3:-1])

#List Methods
#Append (Adds one element at the end)
list = [1,2,3]
list.append(4)
list.append(8)
list.append(7)

#Sort (sorts in ascending order)
list.sort()


print(list)

#sort (sort in decending order)
list.sort(reverse=True)

print(list)

#Reverse
list.reverse()
print(list)


cs_class =["Asim",3.29,"Python"]
cs_class.remove(3.29)
cs_class.pop(0)
print(cs_class)