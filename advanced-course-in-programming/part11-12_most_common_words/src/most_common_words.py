def most_common_words(filename:str,lower_limit:int):
    with open(filename) as thisfile:
        thisfilestring=""
        for line in thisfile:
            parts=line.strip().split()
            thisfilestring+=" ".join(parts)
    words = thisfilestring.split()
    return {word: words.count(word) for word in set(words) if words.count(word)>=lower_limit}
            