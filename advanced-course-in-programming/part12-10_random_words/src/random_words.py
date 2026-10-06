import random

def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        word = ""
        for _ in range(length):
            word += random.choice(characters)
        yield word