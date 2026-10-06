class Car:
    def __init__(self):
        self.__amountofpetrol=0
        self.__odometer=0
    
    def fill_up(self):
        self.__amountofpetrol+=60
    
    def drive(self,km:int):
        if km>self.__amountofpetrol:
            self.__odometer+=self.__amountofpetrol
            self.__amountofpetrol=0
        else:
            self.__amountofpetrol=self.__amountofpetrol-km
            self.__odometer+=km

    def __str__(self):
        return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__amountofpetrol} litres"