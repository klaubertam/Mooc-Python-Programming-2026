n=int(input("How many items: "))
list=[]
i=0
while i<n:
    value=int(input(f"Item {i+1}: "))
    list.append(value)
    i=i+1
print(list)