class DecreasingCounter:
    def __init__(self,initial_value:int):
        self.value=initial_value
    
    def print_value(self):
        print("Value: ", self.value)
    def decrease(self):
        if self.value >0:
            self.value=self.value-1
    def set_to_zero(self):
        self.value=0
    def reset_original_value():
        self.value=self.initial_value
    