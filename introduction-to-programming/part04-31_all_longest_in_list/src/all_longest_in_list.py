def all_the_longest(list):
    newlist=[]
    best=""
    for i in list:
        if len(i) >=len(best):
            best=i
    for i in list:
        if len(i)==len(best):
            newlist.append(i)
    return newlist
if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = all_the_longest(my_list)
    print(result)