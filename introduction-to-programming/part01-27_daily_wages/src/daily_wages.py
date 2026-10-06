wage=float(input("Hourly wage: "))
hours=float(input("Hours worked: "))
day=input("Day of the week: ")
number=wage*hours
if day=="Sunday":
    number=number*2
print(f"Daily wages: {number} euros")