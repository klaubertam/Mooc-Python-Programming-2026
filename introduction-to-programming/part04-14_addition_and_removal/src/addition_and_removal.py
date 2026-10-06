list=[]
i=0
while True:
    print(f"The list is now {list}")
    order=input("a(d)d,(r)remove or e(x)it: ")
    if(order=="d"):
        i=i+1
        list.append(i)
    elif(order=="r"):
        i=i-1
        list.pop(i)
    else:
        print("Bye!")
        break