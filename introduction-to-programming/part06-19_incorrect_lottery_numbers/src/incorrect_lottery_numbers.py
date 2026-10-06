def filter_incorrect():
    with open("lottery_numbers.csv") as lotterynumbers, \
         open("correct_numbers.csv", "w") as correctnumbers:

        for line in lotterynumbers:
            parts = line.strip().split(";")
            if len(parts) != 2:
                continue

            firstpart = parts[0].split(" ")
            secondpart = parts[1].split(",")

            try:
                int(firstpart[1])
            except (ValueError, IndexError):
                continue
            if len(secondpart) < 7:
                continue
            try:
                numbers = [int(n) for n in secondpart]
            except ValueError:
                continue

            if all(1 <= n <= 38 for n in numbers) and len(numbers) == len(set(numbers)):
                correctnumbers.write(line)