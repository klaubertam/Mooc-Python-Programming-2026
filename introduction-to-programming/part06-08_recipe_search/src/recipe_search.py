def readrecipefile(filename: str):
    with open(filename) as recipes:
        mybiglist = [line.strip() for line in recipes]

    anotherbiglist = []
    newlist = []

    for line in mybiglist:
        if line:
            newlist.append(line)
        else:
            anotherbiglist.append(newlist)
            newlist = []

    if newlist:
        anotherbiglist.append(newlist)

    return anotherbiglist
                

def search_by_name(filename: str, word: str):
    namelist = []
    mylist = readrecipefile(filename)

    for recipe in mylist:
        if word.lower() in recipe[0].lower():
            namelist.append(recipe[0])

    return namelist

def search_by_time(filename: str, prep_time: int):
    namelist = []
    mylist = readrecipefile(filename)

    for recipe in mylist:
        if int(recipe[1]) <= prep_time:
            sentence = recipe[0] + ", preparation time " + recipe[1] + " min"
            namelist.append(sentence)

    return namelist

def search_by_ingredient(filename: str, ingredient: str):
    namelist = []
    mylist = readrecipefile(filename)

    for recipe in mylist:
        if ingredient.lower() in [i.lower() for i in recipe[2:]]:
            sentence = recipe[0] + ", preparation time " + recipe[1] + " min"
            namelist.append(sentence)

    return namelist