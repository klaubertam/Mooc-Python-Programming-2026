from random import sample
def words(n: int, beginning: str):
    my_list=[]
    with open("words.txt") as words_file:
        for line in words_file:
            my_list.append(line.strip())
    found_words=[]
    for word in my_list:
        if word.startswith(beginning) and word not in found_words:
            found_words.append(word)
    if len(found_words)<n:
        raise ValueError
    else:
        return sample(found_words, n)