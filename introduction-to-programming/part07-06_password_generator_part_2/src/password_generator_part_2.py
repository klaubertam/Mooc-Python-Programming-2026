from random import choice, shuffle
import string

def generate_strong_password(length: int, numbers: bool, specials: bool):
    chars = string.ascii_lowercase
    numberslist=string.digits
    specialslist="!?=+-()#"
    password = []
    password.append(choice(string.ascii_lowercase))
    if numbers:
        chars += numberslist
        password.append(choice(numberslist))
    if specials:
        chars += specialslist
        password.append(choice(specialslist))

    while len(password) < length:
        password.append(choice(chars))

    shuffle(password)

    return "".join(password)