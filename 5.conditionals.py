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
