# Write your solution here
pin=4321
attempts=0
while True:
    userinput=int(input("PIN: "))
    attempts=attempts+1
    if userinput==4321:
        break
    else:
        print("Wrong")
if attempts==1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
