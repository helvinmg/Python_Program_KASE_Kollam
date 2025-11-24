#Multi Level Inheritance
class Parent:
    def parentDetails(self):
        print("these are the parent details")

class Child(Parent):
    def childDetails(self):
        print("these are the child details")

class Gchild(Child):
    def gChildDetails(self):
        print("these are the grand child details")


obj=Gchild()
obj.gChildDetails()
obj.childDetails()
obj.parentDetails()
