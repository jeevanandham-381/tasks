#multilevel inheritance
class head_of_the_dept:
    def __init__(self,hod):
        self.hod=hod

class Faculty(head_of_the_dept):
    def __init__(self,faculty,hod):
        self.faculty=faculty
        head_of_the_dept. __init__(self,hod)

class Students(Faculty):
    def __init__(self, student,faculty, hod):
            
        self.student=student
        Faculty.__init__(self,faculty,hod)
    
    def details(self):
        print("the dept is:",self.hod)
        print("the faculty is:",self.faculty)
        print("the student is:",self.student)
s=Students("jeeva","thiru","cse")

s.details()                