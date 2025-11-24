#Method Overriding
class Parent:
    def test(self):
        print("test inside parent")
    def parentDetails(self):
        print("these are the parent details")

class Child(Parent):
    def test(self):
        print("test inside child")
    def childDetails(self):
        print("these are the child details")

obj=Child()
obj.childDetails()
obj.parentDetails()
obj.test()
