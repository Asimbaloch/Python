person_a = input ("What is your name: ")
person_b = input ("What is your name: ")

age_a = input ("What is your age: ")
age_b = input ("What is your age: ")

if int(age_a) > int(age_b):
    print(person_a + " is older than " + person_b)
else:
    print(person_b + " is older than " + person_a)


weight = float(input("What is your weight (in kg): "))
height = float(input("What is your height (in m): "))

bmi = weight / (height ** 2)

print("Your BMI is: " + str(bmi))
