# Write your solution here
password=input("Password: ")
while True:
    repeatedPassword=input("Repeat password: ")
    if password==repeatedPassword:
        print("User account created!")
        break
    else:
        print("They do not match!")