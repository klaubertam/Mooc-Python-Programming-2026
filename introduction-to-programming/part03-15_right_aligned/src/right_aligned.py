word=input("Please type in a string: ")
n=20-len(word)
w=""
while n>0:
    w+="*"
    n-=1
print(w+word)