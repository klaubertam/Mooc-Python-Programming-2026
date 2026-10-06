# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.list=[]
    
    def add(self,person: Person):
        self.list.append(person)

    def is_empty(self):
        return len(self.list)==0
    
    def print_contents(self):
        sumi=0
        for person in self.list:
            sumi+=person.height
        print(f"There are {len(self.list)} persons in the room, and their combined height is {sumi} cm")
        for person in self.list:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        if self.is_empty():
            return None
        else:
            mini=500
            shortie=self.list[0]
            for person in self.list:
                if person.height<shortie.height:
                    shortie=person
            return shortie

    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            shortie=self.shortest()
            self.list.remove(shortie)
            return shortie