def largest():
    with open("numbers.txt") as myfile:
        list=[]
        for line in myfile:
            list.append(int(line))
    return max(list)

def main():
    print(largest())

if __name__=="__main__":
    main()