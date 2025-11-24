class Emp:
    def __init__(self,name,desg,sal):
        self.name=name
        self.desg=desg
        self.sal=sal
    def empDisp(self):
        print("Name:",self.name)
        print("Desg:",self.desg)
        print("Salary:",self.sal)
        print("---------------------")
    def incSal(self,amt):
        self.sal=self.sal+amt

emp1=Emp("mahesh","intern",15000)
emp2=Emp("varun","TL",95000)
emp3=Emp("david","Web Developer",65000)
emp4=Emp("veena","Tester",45000)
emps=[emp1,emp2,emp3,emp4]
for e in emps:
    e.empDisp()
emp1.incSal(2500)#Increasing sal of intern
for e in emps:
    e.empDisp()
