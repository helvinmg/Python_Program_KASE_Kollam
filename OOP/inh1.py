#Single Inheritance
class Parent:
    def parentDetails(self):
        print("these are the parent details")

class Child(Parent):
    def childDetails(self):
        print("these are the child details")

obj=Child()
obj.childDetails()
obj.parentDetails()


        
        
