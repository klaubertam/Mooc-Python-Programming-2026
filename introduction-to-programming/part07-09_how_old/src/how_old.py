from datetime import datetime
bday=int(input("Day: "))
bmonth=int(input("Month: "))
byear=int(input("Year: "))

time_now=datetime(byear,bmonth,bday)
millenium=datetime(1999,12,31)

if time_now>millenium:
    print("You weren't born yet on the eve of the new millennium.")
elif time_now<=millenium:
    difference=millenium-time_now
    print(f"You were {difference.days} days old on the eve of the new millennium.")

