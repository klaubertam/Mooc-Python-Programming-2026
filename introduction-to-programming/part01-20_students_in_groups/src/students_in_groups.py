numberOfStudents=int(input("How many students on the course? "))
groupSize=int(input("Desired group size? "))
groups=numberOfStudents//groupSize
leftovers=numberOfStudents%groupSize
if leftovers>0:
 groups+=1


print(f"Number of groups formed: {groups}")