class Parent1:
    def parent1Details(self):
        print("these are the parent details")
    def test(self):
        print("test of parent1")
class Parent2:
    def parent2Details(self):
        print("these are the parent details")
    def test(self):
        print("test of parent2")
class Child(Parent2,Parent1):
    def childDetails(self):
        print("these are the child details")

obj=Child()
obj.childDetails()
obj.parent1Details()
obj.parent2Details()
obj.test()
#resolved using MRO(Method Resolution Order)
#Parent coming first in Inheritance Syntax taken
