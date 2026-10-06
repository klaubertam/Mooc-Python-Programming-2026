def list_of_stars(list):
    for i in list:
        word=""
        while i>0:
            i=i-1
            word=word+"*"
        print(word)
if __name__=="__main__":
    list=[1,2,3,4,5]
    print(list_of_stars(list))