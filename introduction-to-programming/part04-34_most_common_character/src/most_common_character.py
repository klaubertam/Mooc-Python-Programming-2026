def most_common_character(word):
    newlist=[]
    for character in word:
        newlist.append(word.count(character))
    i= max(newlist)
    for character in word:
        if i==word.count(character):
            return character