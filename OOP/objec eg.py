class Student:
    #class attribute
    course="MERN"
    #instance attribute using constructor
    def __init__(self):
        print("constructor is running")
        self.marks=0
    def disp(self):
        print("Course: ",self.course)
        print("Marks: ",self.marks)

stud1=Student()
stud2=Student()
print("stud1.marks",stud1.marks)
stud1.marks=34
print("stud1.marks",stud1.marks)
stud2.marks=38
stud1.disp()
stud2.disp()
