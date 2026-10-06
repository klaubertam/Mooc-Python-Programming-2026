students_file=input("Student information: ")
exercises_file=input("Exercises completed: ")
exam_points=input("Exam points: ")
students={}
with open(students_file) as studentfile:
    for line in studentfile:
        parts=line.strip().split(";")
        if parts[0]=="id":
            continue
        students[parts[0]]=parts[1]+" "+parts[2]

exercises={}
with open(exercises_file) as exercisefile:
    for line in exercisefile:
        parts=line.strip().split(";")
        if parts[0]=="id":
            continue
        exercises[parts[0]]=[]
        for exercise in parts[1:]:
            exercises[parts[0]].append(int(exercise))

exampoints={}
with open(exam_points) as examfile:
    for line in examfile:
        parts=line.strip().split(";")
        if parts[0]=="id":
            continue
        exampoints[parts[0]]=[]
        for points in parts[1:]:
            exampoints[parts[0]].append(int(points))

for id,student in students.items():
    if id in exercises and id in exampoints:
        bonus=(sum(exercises[id]) * 10) // 40
        points=bonus+sum(exampoints[id])
        if points<15:
            grade=0
        elif points<18:
            grade=1
        elif points<21:
            grade=2
        elif points<24:
            grade=3
        elif points<28:
            grade=4
        else:
            grade=5
        print(f"{student} {grade}")
        