# Write your solution here:

class Clock:
    def __init__(self,hours:int,minutes:int,seconds:int):
        self.seconds = seconds
        self.minutes = minutes
        self.hours=hours
    
    def tick(self):
        if self.seconds !=59:
            self.seconds+=1
        elif self.minutes!=59:
            self.minutes+=1
            self.seconds=0
        elif self.hours!=23:
            self.hours+=1
            self.minutes=0
            self.seconds=0
        else:
            self.hours=0
            self.minutes=0
            self.seconds=0
            
    def set(self,thishour:int,thisminute:int):
        self.hours=thishour
        self.minutes=thisminute
        self.seconds=0
        
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"