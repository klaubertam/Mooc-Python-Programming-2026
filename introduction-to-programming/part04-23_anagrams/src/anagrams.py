def anagrams(word1,word2):
    return sorted(word1)==sorted(word2)
if __name__=="__main__":
    print(anagrams("tame","meta"))