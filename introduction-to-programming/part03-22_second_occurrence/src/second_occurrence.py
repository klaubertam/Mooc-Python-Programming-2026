word = input("Please type in a word: ")
char = input("Please type in a substring: ")

count = 0
index = 0

while index < len(word):
    i = word.find(char, index)
    if i == -1:
        break
    count += 1
    if count == 2:
        print(f"The second occurrence of the substring is at index {i}.")
        break
    index = i + len(char)

if count < 2:
        print("The substring does not occur twice in the string.")