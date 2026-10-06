word=input("Please type in a string: ")
n=len(word)-1
if word[1]==word[n-1]:
    print(f"The second and the second to last characters are {word[1]}")
else:
    print("The second and the second to last characters are different")