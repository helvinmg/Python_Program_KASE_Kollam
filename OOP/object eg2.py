class Student:
    #parameterized constructor
    def __init__(self,name="NA",marks=0):
        self.name=name
        self.marks=marks
    def disp(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)

stud1=Student("aromal",37)
stud2=Student("dhiya",38)
stud3=Student()
print("Student 1 Details")
stud1.disp()
print("Student 2 Details")
stud2.disp()
print("Student 3 Details")
stud3.disp()
