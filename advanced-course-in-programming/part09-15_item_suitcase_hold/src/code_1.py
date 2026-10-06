class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.name()} ({self.weight()} kg)"


class Suitcase:
    def __init__(self, maximum_weight: int):
        self.maximum_weight = maximum_weight
        self.listOfItems = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.maximum_weight:
            self.listOfItems.append(item)

    def weight(self):
        return sum(item.weight() for item in self.listOfItems)

    def heaviest_item(self):
        if not self.listOfItems:
            return None
        return max(self.listOfItems, key=lambda item: item.weight())

    def __str__(self):
        count = len(self.listOfItems)
        word = "item" if count == 1 else "items"
        return f"{count} {word} ({self.weight()} kg)"

    def print_items(self):
        for item in self.listOfItems:
            print(item)


class CargoHold:
    def __init__(self, maximum_weight: int):
        self.maximum_weight = maximum_weight
        self.listOfSuitcases = []

    def weight(self):
        return sum(suitcase.weight() for suitcase in self.listOfSuitcases)

    def add_suitcase(self, suitcase: Suitcase):
        if self.weight() + suitcase.weight() <= self.maximum_weight:
            self.listOfSuitcases.append(suitcase)

    def __str__(self):
        space_left = self.maximum_weight - self.weight()
        count = len(self.listOfSuitcases)
        word = "suitcase" if count == 1 else "suitcases"
        return f"{count} {word}, space for {space_left} kg"

    def print_items(self):
        for suitcase in self.listOfSuitcases:
            suitcase.print_items()