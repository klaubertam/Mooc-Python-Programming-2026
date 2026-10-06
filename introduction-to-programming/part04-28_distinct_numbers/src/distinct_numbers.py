def distinct_numbers(mylist):
    newlist=[]
    for i in mylist:
        if i in newlist:
            continue
        else:
            newlist.append(i)
    return sorted(newlist)
if __name__=="__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))