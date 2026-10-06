class Person:
    def __init__(self,name:str):
        self.name=name
    
    def return_first_name(self):
        first=self.name.split()
        return first[0]
    
    def return_last_name(self):
        last=self.name.split()
        return last[1]
