#Odd and Even Program

number = int (input ("Please enter the number :"))

if number % 2 == 0 :
    print("It is even")
else:
    print("Your number is odd")

#Profit and loss program

cost_price = int (input("what is the cost price: "))

sell_price = int (input("what is the sell price: "))


if sell_price >cost_price:
    profit = sell_price - cost_price
    print("The seller earned :",profit)
else:
    loss = cost_price - sell_price
    print ("the seller has the loss of ", loss)

#Grade
student_marks = int (input("Please write your numbers :"))
marks_percentage = student_marks * 100 / 100
if marks_percentage >= 80:
    print("Very good")

elif marks_percentage >=61:
    print("Good")

elif marks_percentage >=41:
    print("Average")

#Traffic Light Program
light_color = input ("What is the color of the light?")

if (light_color =="green"):
    print ("You can go")

elif (light_color=="red"):
    print("You can not go.")

else:
    print("Light is broken.")
