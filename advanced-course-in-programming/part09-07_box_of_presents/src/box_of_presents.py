# WRITE YOUR SOLUTION HERE:
class Present:
    def __init__(self,name:str,weight:int):
        self.name=name
        self.weight=weight
    
    def __str__(self):
        return f"{self.name} ({self.weight} kg)"
class Box:
    def __init__(self):
        self.list=[]

    def add_present(self,present:Present):
        self.list.append(present)

    def total_weight(self):
        totalweight=0
        for present in self.list:
            totalweight+=present.weight
        return totalweight