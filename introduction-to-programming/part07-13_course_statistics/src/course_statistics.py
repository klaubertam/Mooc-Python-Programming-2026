import urllib.request
import json
import math
def retrieve_all():
    request=urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    content = json.loads(request.read())
    enabled_courses=[]
    for element in content:
        if element["enabled"]:
            enabled_courses.append((element["fullName"],element["name"],element["year"],sum(element["exercises"])))
    return enabled_courses

def retrieve_course(course_name: str):
    mylink = f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course_name}/stats"
    request=urllib.request.urlopen(mylink)
    content = json.loads(request.read())
    weeks=len(content)
    students=0
    hours_total=0
    exercises=0
    for element in content.values():
        students=max(students,element["students"])
        hours_total+=element["hour_total"]
        exercises+=element["exercise_total"]
    hours_average=math.floor(hours_total/students)
    exercises_average=math.floor(exercises/students)
    newdictionary={}
    newdictionary["weeks"]=weeks
    newdictionary["students"]=students
    newdictionary["hours"]=hours_total
    newdictionary["hours_average"]=hours_average
    newdictionary["exercises"]=exercises
    newdictionary["exercises_average"]=exercises_average
    return newdictionary