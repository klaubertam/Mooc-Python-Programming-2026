def find_words(search_term: str):
    result = []

    with open("words.txt") as wordslist:
        for word in wordslist:
            word = word.strip()

            if "*" not in search_term and "." not in search_term:
                if word == search_term:
                    result.append(word)

            elif search_term.startswith("*"):
                if word.endswith(search_term[1:]):
                    result.append(word)

            elif search_term.endswith("*"):
                if word.startswith(search_term[:-1]):
                    result.append(word)

            elif "." in search_term:
                if len(word) != len(search_term):
                    continue
                
                match = True
                for i in range(len(search_term)):
                    if search_term[i] != "." and search_term[i] != word[i]:
                        match = False
                        break
                
                if match:
                    result.append(word)

    return result