# A function is a block of code which only runs when it is called.

#You can pass data, known as parameters, into a function.

#A function can return data as a result.

#Functions are defined using the def keyword

def greet_user():
    print("Hello")


greet_user()


def greet(name):
    print("hello " + name)

greet("asim")


#return values

def square(number):
    return number * number

print(square(5))

#recursion function

def count_down(number):
    if number <= 0:
        print("Done!")
    else:
        print(number)
        count_down(number - 1)

count_down(5) 