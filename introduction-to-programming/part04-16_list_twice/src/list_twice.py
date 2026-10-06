list=[]
while True:
    newvalue=int(input("New item: "))
    if newvalue!=0:
        list.append(newvalue)
        print(f"The list now: {list}")
        print(f"The list in order: {sorted(list)}")
    else:
        print("Bye!")
        break
