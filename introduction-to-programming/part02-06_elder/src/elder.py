# Write your solution here
print("Person 1:")
name1=input("Name: ")
number1=int(input("Age: "))
print("Person 2:")
name2=input("Name: ")
number2=int(input("Age: "))
if number1<number2:
    print(f"The elder is {name2}")
elif number1>number2:
    print(f"The elder is {name1}")
elif number1==number2:
    print(f"{name1} and {name2} are the same age")