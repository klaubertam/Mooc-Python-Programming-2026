first=input("1st letter: ")
second=input("2nd letter: ")
third=input("3rd letter: ")
middle=0
if first<second<third or first>second>third:
    middle=second
elif first<third<second or first>third>second:
    middle=third
elif second<first<third or second>first>third:
    middle=first
print(f"The letter in the middle is {middle}")