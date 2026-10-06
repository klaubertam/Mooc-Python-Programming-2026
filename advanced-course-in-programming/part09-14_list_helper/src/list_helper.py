# WRITE YOUR SOLUTION HERE:
class ListHelper:

    @classmethod
    def greatest_frequency(cls,my_list: list):
        dictionary={}
        for element in my_list:
            dictionary[element]=my_list.count(element)
        return max(dictionary,key=dictionary.get)
    
    @classmethod
    def doubles(cls,my_list: list):
        count=0
        thislist=[]
        for element in my_list:
            if element not in thislist and my_list.count(element)>=2:
                count+=1
                thislist.append(element)
        return count
