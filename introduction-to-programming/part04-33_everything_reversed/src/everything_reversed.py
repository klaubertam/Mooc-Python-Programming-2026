def everything_reversed(list):
    newlist=[]
    for word in list:
        newlist.append(word[::-1])
    return newlist[::-1]