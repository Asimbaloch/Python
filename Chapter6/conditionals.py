age = int (input("What is your age: "))

if (age>18):
    print("you can vote")

elif(age<0):
    print("Your age is invalid.")


elif(age==0):
    print("You are entering 0 which is invalid age.")

else:
    print("You can not vote.")