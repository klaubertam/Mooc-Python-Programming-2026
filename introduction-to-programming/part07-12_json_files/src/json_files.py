import json
def print_persons(filename: str):
    with open(filename) as my_file:
        data=my_file.read()
    people=json.loads(data)
    for person in people:
        hobbiesnew=""
        for hobby in person["hobbies"]:
            hobbiesnew+=hobby+", "
        hobbiesnew=hobbiesnew[:-2]+")"

        print(f"{person["name"]} {person["age"]} years ({hobbiesnew}")