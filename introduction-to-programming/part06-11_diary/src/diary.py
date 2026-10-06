while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    entry=int(input("Function: "))
    if entry==0:
        print('Bye now!')
        break
    elif entry==1:
        sentence=input("Diary entry: ")
        with open("diary.txt","a") as mydiary:
            mydiary.write(sentence)
            mydiary.write("\n")
            print("Diary saved")
    elif entry==2:
        print("Entries:")
        with open("diary.txt") as mydiary:
            for line in mydiary:
                print(line.strip())
