import string

def separate_characters(my_string: str):
    letters = ""
    punctuation_chars = ""
    others = ""

    for char in my_string:
        if char in string.ascii_letters:
            letters += char
        elif char in string.punctuation:
            punctuation_chars += char
        else:
            others += char

    return (letters, punctuation_chars, others)