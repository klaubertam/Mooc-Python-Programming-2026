from random import choice
import string

def generate_password(length:int):
    password=""
    while len(password)<length:
        password +=choice(string.ascii_lowercase)
    return password