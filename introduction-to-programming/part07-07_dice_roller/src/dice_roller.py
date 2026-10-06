from random import choice

def roll(die:str):
    if die=="A":
        list=[3,3,3,3,3,6]
        output=choice(list)
    if die=="B":
        list=[2,2,2,5,5,5]
        output=choice(list)
    if die=="C":
        list=[1,4,4,4,4,4]
        output=choice(list)
    return output

def play(die1:str,die2:str,times:int):
    die1_count=0
    die2_count=0
    tie=0
    for i in range(times):
        die1_result=roll(die1)
        die2_result=roll(die2)
        if die1_result>die2_result:
            die1_count+=1
        elif die1_result<die2_result:
            die2_count+=1
        else:
            tie+=1
    return (die1_count,die2_count,tie)