class Student:
    #class attribute/variables
    #one copy is shared among all objects
    course="MERN"
    def disp(self):
        print("Course: ",self.course)

anson=Student()
print(anson)
anson.disp()
arun=Student()
arun.disp()
#we will modify it using class name
Student.course="FS"
anson.disp()
arun.disp()
