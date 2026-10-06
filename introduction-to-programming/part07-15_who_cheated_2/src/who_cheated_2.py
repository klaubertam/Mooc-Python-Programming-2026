from datetime import datetime, timedelta

def final_points():
    start_times = {}
    with open("start_times.csv") as f:
        for line in f:
            name, start = line.strip().split(";")
            start_times[name] = datetime.strptime(start, "%H:%M")
    scores = {}

    with open("submissions.csv") as f:
        for line in f:
            name, task, points, time = line.strip().split(";")

            if name not in start_times:
                continue

            submit_time = datetime.strptime(time, "%H:%M")
            diff = submit_time - start_times[name]

            if diff > timedelta(hours=3):
                continue

            points = int(points)

            if name not in scores:
                scores[name] = {}

            if task not in scores[name]:
                scores[name][task] = points
            else:
                scores[name][task] = max(scores[name][task], points)

    result = {}

    for name in scores:
        result[name] = sum(scores[name].values())

    return result