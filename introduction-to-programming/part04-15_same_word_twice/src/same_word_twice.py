words=[]
while True: 
    newword=input("Word: ")
    if newword in words:
        break
    else:
        words.append(newword)
print(f"You typed in {len(words)} different words")