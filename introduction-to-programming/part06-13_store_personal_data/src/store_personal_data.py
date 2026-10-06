def store_personal_data(person: tuple):
    name=person[0]
    age=person[1]
    height=person[2]
    line=f"{name};{age};{height}"
    with open("people.csv","a") as people_file:
        people_file.write(line)