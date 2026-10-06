from datetime import datetime,timedelta
def cheaters():
    start_times={}
    cheaters=[]
    with open("start_times.csv") as start:
        for line in start:
            name,starting=line.strip().split(";")
            start_times[name]=datetime.strptime(starting, "%H:%M")
    with open("submissions.csv") as end:
        for line in end:
            name,task,points,ending=line.strip().split(";")
            ending=datetime.strptime(ending,"%H:%M")
            if name in start_times:
                difference=ending-start_times[name]
                if difference>timedelta(hours=3) and name not in cheaters:
                    cheaters.append(name)
    return cheaters