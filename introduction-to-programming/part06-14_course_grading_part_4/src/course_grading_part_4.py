students_file=input("Student information: ")
exercises_file=input("Exercises completed: ")
exam_file=input("Exam points: ")
course_file=input("Course information:")

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
with open(exam_file) as examfile:
    for line in examfile:
        parts=line.strip().split(";")
        if parts[0]=="id":
            continue
        exampoints[parts[0]]=[]
        for points in parts[1:]:
            exampoints[parts[0]].append(int(points))

coursename=""
coursecredits=0
with open(course_file) as coursefile:
    for line in coursefile:
        parts=line.strip().split(":")
        if parts[0]=="name":
            coursename=parts[1].strip()
        if parts[0]=="study credits":
            coursecredits=int(parts[1])



with open("results.txt","w") as results1:
    results1.write(f"{coursename}, {coursecredits} credits\n")
    results1.write("======================================\n")
    results1.write("name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade\n")

    for id,student in students.items():
        if id in exercises and id in exampoints:
            total_exercises=sum(exercises[id])
            bonus=(sum(exercises[id]) * 10) // 40
            exam_points=sum(exampoints[id])
            points=bonus+exam_points
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
            results1.write(f"{student:<29} {total_exercises:<8}  {bonus:<9} {exam_points:<8}  {points:<8}  {grade}\n")        


with open("results.csv","w") as results2:
    for id,student in students.items():
        if id in exercises and id in exampoints:
            total_exercises=sum(exercises[id])
            bonus=(sum(exercises[id]) * 10) // 40
            exam_points=sum(exampoints[id])
            points=bonus+exam_points
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
            results2.write(f"{id};{student};{grade}\n")