number1=int(input("Number1: "))
number2=int(input("Number2: "))
operation=input("Operation: ")
print()
newnumber=0
if operation=="add":
    newnumber=number1+number2
    print(f"{number1} + {number2} = {newnumber}")
if operation=="multiply":
    newnumber=number1*number2
    print(f"{number1} * {number2} = {newnumber}")
if operation=="subtract":
    newnumber=number1-number2
    print(f"{number1} - {number2} = {newnumber}")