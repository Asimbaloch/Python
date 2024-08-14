#Indentation in Python
if True:
    print("True")
    print("True")

print("This is outside the if block")

if False:
    print("False")
else:
    print("Else block")

print("This is outside the if block")

if True:
    print("True")
    if False:
        print("False")
    else:
        print("Else block")

print("This is outside the if block")

if True:
    print("True")
    if True:
        print("True")
    else:
        print("Else block")

print("This is outside the if block")

if True:
    print("True")
    if False:
        print("False")

print("This is outside the if block")
