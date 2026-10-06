def shortest(mylist):
    best="jkhfgsdfgweahfhfgyuasyfgdsygfjdsgfhgdshgfghds"
    for i in mylist:
        if len(i) <=len(best):
            best=i
    return best
if __name__=="__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = shortest(my_list)
    print(result)