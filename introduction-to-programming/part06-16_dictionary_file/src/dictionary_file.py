while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    entry=int(input("Function: "))
    if entry==3:
        print('Bye!')
        break
    elif entry==1:
        finishword=input("The word in Finnish: ")
        englishword=input("The word in English: ")
        with open("dictionary.txt","a") as mydictionary:
            mydictionary.write(f"{finishword} - {englishword}\n")
            print("Dictionary entry added")
    elif entry==2:
        search_term=input("Search term:")
        with open("dictionary.txt") as mydictionary:
            for line in mydictionary:
                if search_term in line:
                    print(line)