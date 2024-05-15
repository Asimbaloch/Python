#While loops
count=1
while count<=5:
    print("Hello everyone!")
    count+=1

    i=1
    while i <= 5:
        print("check")
        i+=1




#Q - Print numbers from 1 to 100.
i = 1
while i<=100:
    print(i)
    i+=1

#Q - Print numbers from 100 to 1.

num1 = 100
while num1>=1:
    print(num1)
    num1 -=1

#WAP to write the multiplication table.
n=int(input("Please enter the number."))
t = 1
while t<=10:
    print(n*t)
    t+=1

#WAP to print the elements of the loop.
nums =[1,4,9,16,25,36,49,64,81,100]

idx= 0

while idx < len(nums):
    print(nums[idx])
    idx+=1

#Search for a number x in this tuple using loop"
roll_numbers = (1,4,9,16,25,36,49,64,81,100)
x=16
i = 0
while i<len(roll_numbers):
    if (nums[i]==x):
        print("Found at", i)
    i+=1
