word = input("Please type in a word: ")
char = input("Please type in a character: ")
index=word.find(char)
if index>=0 and len(word)-index>=3:
    print(word[index:index+3])