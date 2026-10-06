import difflib
def correct(word):
    mywordlist=[]
    with open("wordlist.txt") as wordfile:
        for line in wordfile:
            mywordlist.append(line.strip())
    if word.lower() in mywordlist:
        return True
    else:
        matches_list=difflib.get_close_matches(word.lower(),mywordlist)
        return matches_list


sentence=input("Write text: ")
newsentence=""
suggestions={}
for word in sentence.split():
    result = correct(word)
    if result == True:
        newsentence += word + " "
    else:
        newsentence += "*" + word + "*" + " "
        suggestions[word] = result

print(newsentence)
print("suggestions: ")
for key,value in suggestions.items():
    print(f"{key}: {', '.join(value)}")