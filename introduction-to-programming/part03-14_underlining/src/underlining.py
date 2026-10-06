while True:
    word=input("Please type in a string: ")
    n=len(word)
    w=""
    if n==0:
        break
    else:
        print(word)
        while n>0:
            w+="-"
            n-=1
        print(w)