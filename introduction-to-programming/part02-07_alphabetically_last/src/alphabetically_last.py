# Write your solution here
name1=input("Please type in the 1st word: ")
name2=input("Please type in the 2nd word: ")
if name1<name2:
    print(f"{name2} comes alphabetically last.")
elif name1>name2:
    print(f"{name1} comes alphabetically last.")
elif name1==name2:
    print("You gave the same word twice.")