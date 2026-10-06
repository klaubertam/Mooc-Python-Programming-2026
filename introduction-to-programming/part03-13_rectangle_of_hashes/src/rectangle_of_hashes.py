width=int(input("Width: "))
height=int(input("Height: "))
w=""
while height>0:
    while width>0:
        w+="#"
        width-=1
    height-=1
    print(w)