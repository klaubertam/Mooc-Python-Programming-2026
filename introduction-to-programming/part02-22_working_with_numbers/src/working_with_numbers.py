print("Please type in integer numbers. Type in 0 to finish.")
count=0
sum=0
p=0
n=0
while True:
    number=int(input("Number: "))
    if number==0:
        break
    else:
        count=count+1
        sum=sum+number
        if number<0:
            n=n+1
        else:
            p=p+1
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {float(sum/count)}")
print(f"Positive numbers {p}")
print(f"Negative numbers {n}")
