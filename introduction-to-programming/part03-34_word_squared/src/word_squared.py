def squared(text, size):
    n = len(text)
    repeated = text * (size * 2)

    for i in range(size):
        start = (i * size) % n
        print(repeated[start:start+size])
if __name__ == "__main__":
     squared("abc",5)