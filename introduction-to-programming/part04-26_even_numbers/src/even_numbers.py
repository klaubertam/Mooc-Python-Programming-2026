def even_numbers(list):
    newlist=[]
    for i in list:
        if i%2==0:
            newlist.append(i)
    return newlist
if __name__=="__main__":
    list=[1,2,3,4,5]
    print("original", list)
    print("new", even_numbers(list))