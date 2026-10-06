def same_chars(word, x, y):
    if x<0 or y< 0 or x>len(word)-1 or y>len(word)-1:
        return False
    else:
        return word[x] == word[y]


if __name__ == "__main__":
    print(same_chars("coder", 1, 2))