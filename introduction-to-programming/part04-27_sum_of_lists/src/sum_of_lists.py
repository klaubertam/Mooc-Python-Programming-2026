def list_sum(list1,list2):
    sumlist=[]
    for i in range(0,len(list1)):
        sum=list1[i]+list2[i]
        sumlist.append(sum)
    return sumlist
if __name__=="__main__":
    list1=[1,2,3,4,5]
    list2=[1,2,3,4,5]
    print(list_sum(list1,list2))