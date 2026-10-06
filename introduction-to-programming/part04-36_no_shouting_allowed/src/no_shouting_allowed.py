def no_shouting(list):
    newlist=[]
    for word in list:
        if word.isupper()!=True:
            newlist.append(word)
    return newlist