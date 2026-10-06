def exam_points_and_exercises():
    points = []
    exercises = []

    while True:
        line = input("Exam points and exercises completed: ")

        if line == "":
            break

        p, e = line.split()
        points.append(int(p))
        exercises.append(int(e))

    return points, exercises


def statistics(points, exercises):
    grades = []
    total_points_sum = 0
    failures = 0

    for i in range(len(points)):
        total = points[i] + exercises[i] // 10
        if total < 15 or points[i]<10:
            grades.append(0)
            failures += 1
        elif total < 18:
            grades.append(1)
        elif total < 21:
            grades.append(2)
        elif total < 24:
            grades.append(3)
        elif total < 28:
            grades.append(4)
        else:
            grades.append(5)

        total_points_sum += total

    print("Statistics:")
    print(f"Points average: {total_points_sum / len(points):.1f}")
    print(f"Pass percentage: {(len(points) - failures) / len(points) * 100:.1f}")
    print("Grade distribution:")

    for g in range(5, -1, -1):
        print(f"{g}: {'*' * grades.count(g)}")


# MAIN PROGRAM
points, exercises = exam_points_and_exercises()
statistics(points, exercises)