# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    count1=0
    for keys, values in person1.items():
        if keys !="name":
            count1+=values
    average1=float(count1/3)
        
    count2=0
    for keys, values in person2.items():
        if keys !="name":
            count2+=values
    average2=float(count2/3)
    
    count3=0
    for keys, values in person3.items():
        if keys !="name":
            count3+=values
    average3=float(count3/3)
        
    if average1<average3 and average1<average2:
        return person1
    elif average3<average2:
        return person3
    else:
        return person2