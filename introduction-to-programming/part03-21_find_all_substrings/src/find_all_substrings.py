word = input("Please type in a word: ")
char = input("Please type in a character: ")

index = 0
while index < len(word):
    i = word.find(char, index)
    if i == -1:
        break  # stop if no more occurrences
    if i + 3 <= len(word):  # ensure there are at least 3 chars from this point
        print(word[i:i+3])
    index = i + 1  # move past this occurrence