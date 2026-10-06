number=int(input("Please type in a number: "))
while number>0:
    factorial=1
    n=number
    while n>0:
        factorial=factorial*n
        n=n-1
    print(f"The factorial of the number {number} is {factorial}")
    number=int(input("Please type in a number: "))
print("Thanks and bye!")