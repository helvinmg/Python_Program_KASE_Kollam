#Method Overloading
class Emp:
    def disp(self):
        print("Employee Details")
        
class Student:
    def disp(self):
        print("Student Details")

obj1=Emp()
obj1.disp()
obj2=Student()
obj2.disp()
#same disp function behave differently
#based on calling object
