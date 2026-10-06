class NumberStats:
    def __init__(self):
        self.numbers=[]
    def add_number(self,number:int):
        self.numbers.append(number)
    def count_numbers(self):
        return len(self.numbers)
    def get_sum(self):
        return sum(self.numbers)
    def average(self):
        if self.count_numbers() == 0:
            return 0
        return self.get_sum() / self.count_numbers()
def main():
    print("Please type in integer numbers: ")
    stati=NumberStats()
    sumodd=0
    sumeven=0
    while True:
        number=int(input())
        if number==-1:
            print(f"Sum of numbers: {stati.get_sum()}")
            print(f"Mean of numbers: {stati.average()}")
            print(f"Sum of even numbers: {sumeven}")
            print(f"Sum of odd numbers: {sumodd}")
            break
        else:
            stati.add_number(number)
            if number%2==0:
                sumeven+=number
            else:
                sumodd+=number
main()