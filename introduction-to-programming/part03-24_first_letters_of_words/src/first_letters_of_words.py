text=input("Please type in a sentence: ")
n=len(text)
print(text[0])
i=0
while i<n:
    if " " in text[i]:
        print(text[i+1])
    i=i+1