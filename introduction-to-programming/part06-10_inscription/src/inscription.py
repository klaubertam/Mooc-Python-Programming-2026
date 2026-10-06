name=input("Whom should I sign this to: ")
location=input("Where shall I save it: ")
with open(location,"w") as myfile:
    myfile.write("Hi "+ name+", we hope you enjoy learning Python with us! Best, Mooc.fi Team")