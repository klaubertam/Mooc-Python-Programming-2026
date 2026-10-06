def spruce(n):
    print("a spruce!")
    i=1
    m=n
    while n>0:
        print((n-1)*" "+i*"*")
        n=n-1
        i=i+2
    print((m-1)*" "+"*")
    
if __name__ == "__main__":
    spruce(5)