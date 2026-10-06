upperlimit=int(input("Limit: "))
sum=0
number=1
story="1 "
while sum<upperlimit:
    sum=sum+number
    number=number+1
    if sum<upperlimit:
        story=story+f"+ {number} "
print(f"The consecutive sum: {story}= {sum}")