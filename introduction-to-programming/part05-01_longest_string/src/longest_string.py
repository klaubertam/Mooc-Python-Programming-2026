def longest(strings: list):
    max=""
    for word in strings:
        if len(word)>=len(max):
            max=word
    return max        
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))    