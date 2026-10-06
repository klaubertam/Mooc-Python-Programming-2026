temp=int(input("Please type in a temperature (F): "))
newtemp=(temp - 32) * 5/9
print(f"{temp} degrees Fahrenheit equals {newtemp} degrees Celsius")
if newtemp<0:
    print("Brr! It's cold in here!")
