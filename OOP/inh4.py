#Hierarchical Inheritance
class Parent:
    def parentDetails(self):
        print("these are the parent details")

class Child1(Parent):
    def child1Details(self):
        print("these are the child1 details")

class Child2(Parent):
    def child2Details(self):
        print("these are the child2 details")

obj1=Child1()
obj1.child1Details()
obj1.parentDetails()
obj2=Child2()
obj2.child1Details()
obj2.parentDetails()
