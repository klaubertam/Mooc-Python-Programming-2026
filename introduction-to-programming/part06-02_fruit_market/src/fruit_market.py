def read_fruits():
    with open("fruits.csv") as my_file:
        mydict={}
        for line in my_file:
            parts=line.split(";")
            mydict[parts[0]]=float(parts[1])
    return mydict
if __name__=="__main__":
    print(read_fruits())