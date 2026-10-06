def read_input(sentence:str,a:int,b:int):
    while True:
        try:
            input_str = input(sentence)
            number = int(input_str)
            if number < b and number >a:
                return number
        except ValueError:
            pass 

        print(f"You must type in an integer between {a} and {b}")