def first_word(sentence):
    word=sentence.split()
    return word[0]
def second_word(sentence):
    word=sentence.split()
    return word[1]
def last_word(sentence):
    word=sentence.split()
    return word[len(word)-1]


if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))