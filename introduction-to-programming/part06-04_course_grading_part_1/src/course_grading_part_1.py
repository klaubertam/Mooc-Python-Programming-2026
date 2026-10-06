if True:
    student_info = input("Student information: ")
    exercise_data = input("Exercises completed: ")
else:
    student_info = "students1.csv"
    exercise_data = "exercises1.csv"
names={}
with open("src/"+student_info) as f1:
    for line in f1:
        line=line.strip()
        parts=line.split(";")
        if parts[0]=="id":
            continue
        else:
            names[parts[0]]=parts[1]+" "+parts[2]
exercises_completed={}
with open("src/"+exercise_data) as f2:
    for line in f2:
        line=line.strip()
        parts=line.split(";")
        if parts[0]=="id":
            continue
        else:
            exercises_completed[parts[0]]=sum(map(int,parts[1:]))
for key,value in names.items():
    if key in exercises_completed:
        print(value+str(exercises_completed[key]))