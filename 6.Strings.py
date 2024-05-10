#Strings
statement =" Hello everyone! I am writing this string to print the string here.\n It is the new line."

print (statement)

#Concatenation
first_name ="Asim"
print(first_name.replace("Asim","Ahsan"))
last_name ="Khan"

complete_name= first_name +" " +last_name
print(complete_name.capitalize())


#Length of String
print(len(complete_name))

print (len(first_name))



#Indexing
university_name = "Lahore School of Computer Sciences"
print (university_name[3])

#Slicing
print(university_name[3:6])
print(university_name[1:4])
print(university_name[7:])
print(university_name[-5:-1]) 

#Q- WAP to input user's first name and print its length.

user_Name=input("What is your good name :")
print(len(user_Name))

#Q- WAP to find the occurance of '$' in String.
ticker= " This is the $ value today"
print(ticker.count("$"))