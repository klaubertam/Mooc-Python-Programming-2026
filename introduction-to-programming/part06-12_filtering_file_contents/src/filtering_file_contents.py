def filter_solutions():
    with open("solutions.csv") as solutions_file, \
         open("correct.csv", "w") as correct, \
         open("incorrect.csv", "w") as incorrect:
        for line in solutions_file:
            parts=line.split(";")
            if "+" in parts[1]:
                numbers=parts[1].split("+")
                end=int(numbers[0])+int(numbers[1])
            elif "-" in parts[1]:
                numbers=parts[1].split("-")
                end=int(numbers[0])-int(numbers[1])
            if end==int(parts[2]):
                correct.write(line)
            else:
                incorrect.write(line)