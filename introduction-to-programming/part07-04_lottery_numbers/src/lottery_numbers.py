from random import randint
def lottery_numbers(amount: int, lower: int, upper: int):
    lottery_list=[]
    while len(lottery_list)<amount:
        newnumber=randint(lower,upper)
        if newnumber not in lottery_list:
            lottery_list.append(newnumber)
    return sorted(lottery_list)