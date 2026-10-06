def sum_of_positives(list):
    sum=0
    for i in list:
        if i>0:
            sum=sum+i
    return sum
if __name__=="__main__":
    list=[1,2,3,4,5]
    print("The result is ",sum_of_positives(list))