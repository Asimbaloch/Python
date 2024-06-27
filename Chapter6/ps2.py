subject1 = int(input("Write the number: "))
subject2 = int(input("Write the number: "))
subject3 = int(input("Write the number: "))

total_percentage = (subject1 + subject2 + subject3) / 3  #Calculate percentage out of 100

if (total_percentage >= 40 and subject1>33 and subject2>33 and subject3>33 ):
    print("You are passed")
else:
    print("Try next time.")
