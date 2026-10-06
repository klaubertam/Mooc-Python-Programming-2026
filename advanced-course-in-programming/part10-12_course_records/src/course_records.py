class Course:
    def __init__(self,course_name:str,course_grade:int,course_credits:int):
        self.course_name=course_name
        self.course_grade=course_grade
        self.course_credits=course_credits
    
    def change_course_grade(self,newgrade:int):
        if self.course_grade<newgrade:
            self.course_grade=newgrade
            
class CourseList:
    def __init__(self):
        self.course_list={}
        
    def add_course(self,courseName:str,courseGrade:int,courseCredits:int):
        if courseName in self.course_list:
            self.course_list[courseName].change_course_grade(courseGrade)
        else:
            course=Course(courseName,courseGrade,courseCredits)
            self.course_list[courseName]=course
                
    def search_course(self,courseName:str):
        if courseName in self.course_list:
            cR=self.course_list[courseName].course_credits
            gR=self.course_list[courseName].course_grade
            print(f"{courseName} ({cR} cr) grade {gR}")
        else:
            print("no entry for this course")
            
    def statistics(self):
        total_credits = 0
        gradesum = 0
        listing = [""] * 5

        for value in self.course_list.values():
            total_credits += value.course_credits
            gradesum += value.course_grade
            listing[value.course_grade - 1] += "x"

        print(f"{len(self.course_list)} completed courses, a total of {total_credits} credits")

        if total_credits > 0:
            print(f"mean {gradesum / len(self.course_list):.1f}")
        else:
            print("mean 0")

        print("grade distribution")

        for i in range(4, -1, -1):
            print(f"{i+1}: {listing[i]}")
        
        
class CourseApplication:
    def __init__(self):
        self.courselist=CourseList()
        
    def go(self):
        print("1 add course")
        print("2 get course data")
        print("3 statistics")
        print("0 exit")
        while True:
            print()
            command=input("command: ")
            if command=="1":
                coursename=input("course: ")
                coursegrade=int(input("grade: "))
                coursecredits=int(input("credits: "))
                self.courselist.add_course(coursename,coursegrade,coursecredits)
            elif command=="2":
                coursename=input("course: ")
                self.courselist.search_course(coursename)
            elif command=="3":
                self.courselist.statistics()
            elif command=="0":
                break

courseapp=CourseApplication()
courseapp.go()