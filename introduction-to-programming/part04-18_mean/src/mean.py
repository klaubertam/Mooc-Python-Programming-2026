def mean(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list[i]
    return sum/len(list)

if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)