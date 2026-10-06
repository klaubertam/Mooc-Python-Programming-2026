class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def days(self):
        return self.year * 360 + self.month * 30 + self.day

    def __lt__(self, another):
        return self.days() < another.days()

    def __gt__(self, another):
        return self.days() > another.days()

    def __eq__(self, another):
        return self.days() == another.days()

    def __ne__(self, another):
        return self.days() != another.days()

    def __add__(self, days: int):
        total = self.days() + days

        year = total // 360
        total %= 360

        month = total // 30
        total %= 30

        day = total

        # fix zero cases
        if day == 0:
            day = 30
            month -= 1

        if month == 0:
            month = 12
            year -= 1

        return SimpleDate(day, month, year)

    def __sub__(self, another):
        return abs(self.days() - another.days())