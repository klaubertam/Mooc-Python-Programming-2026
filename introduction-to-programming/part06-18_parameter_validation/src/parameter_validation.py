def new_person(name: str, age: int):
    parts=name.split(" ")
    wordcount=len(parts)
    charinword=len(name)-wordcount-1
    if not name:
        raise ValueError("The input is empty")
    elif wordcount<2 or charinword>40:
        raise ValueError("The input is invalid")
    elif age<0 or age>150:
       raise ValueError("The input is invalid")
    return (name,age)
