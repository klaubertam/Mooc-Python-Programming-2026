# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        return f"{self.__euros+self.__cents*0.01:.2f} eur"

    def  __eq__(self, another):
        return (self.__euros+self.__cents*0.01)==(another.__euros+another.__cents*0.01)
    
    def __lt__(self, another):
        return (self.__euros+self.__cents*0.01)<(another.__euros+another.__cents*0.01)
    
    def __gt__(self, another):
        return (self.__euros+self.__cents*0.01)>(another.__euros+another.__cents*0.01)
    
    def __ne__(self, another):
        return (self.__euros+self.__cents*0.01)!=(another.__euros+another.__cents*0.01)
    
    def __add__(self, another):
        eurros=self.__euros+another.__euros
        sentts=self.__cents+another.__cents
        their_sum=Money(eurros,sentts)
        return their_sum
    
    def __sub__(self, another):
        if self<another:
            raise ValueError("a negative result is not allowed")
        else:
            eurros=self.__euros-another.__euros
            sentts=self.__cents-another.__cents
            their_sub=Money(eurros,sentts)
        return their_sub    
    