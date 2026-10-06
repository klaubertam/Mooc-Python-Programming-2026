def chessboard(x):
    i=1
    j=1
    a=""
    b=""
    while i<=x:
        if i%2!=0:
            a=a+"0"
            b=b+"1"
        else:
            a=a+"1"
            b=b+"0"
        i=i+1
    while j<=x:
        if j%2==0:
            print(a)
        else:
            print(b)
        j=j+1

if __name__ == "__main__":
    chessboard(6)