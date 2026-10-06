from datetime import date
def is_it_valid(pic: str):
    if len(pic)!=11:
        return False
    dateOfBirth=pic[:2]
    monthOfBirth=pic[2:4]
    yearOfBirth=pic[4:6]
    identifier=pic[:6]+pic[7:10]
    century=pic[6:7]
    if century=="+":
        yearOfBirth="18"+yearOfBirth
    elif century=="-":
        yearOfBirth="19"+yearOfBirth
    elif century=="A":
        yearOfBirth="20"+yearOfBirth
    else:
        return False
    controlcheck=int(identifier)%31
    checkers="0123456789ABCDEFHJKLMNPRSTUVWXY"
    letters=list(checkers)
    
    try:
        date(int(yearOfBirth),int(monthOfBirth),int(dateOfBirth))
        z=letters[controlcheck]
        if z!=pic[10]:
            return False
        return True
    except ValueError:
        return False