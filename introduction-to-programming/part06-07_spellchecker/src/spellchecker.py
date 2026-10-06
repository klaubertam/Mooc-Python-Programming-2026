with open("src/wordlist.txt") as f:
    wordlist=[]
    for line in f:
        wordlist.append(line.strip())
sentence=input("Write text: ")
newsentence=""
for word in sentence.split(" "):
    if word.lower() not in wordlist:
        newsentence+="*"+word+"*"+" "
    else:
        newsentence+=word+" "
print(newsentence)