story=""
newword=""
word=input("Please type in a word: ")
if word!="end":
    story=word
while True:
    newword=input("Please type in a word: ")
    if newword=="end":
        break
    elif newword==word:
        break
    else:
        story=story+" "+newword
        word=newword
print(story)