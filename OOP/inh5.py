#Multiple Inheritance
class Parent1:
    def parent1Details(self):
        print("these are the parent details")
class Parent2:
    def parent2Details(self):
        print("these are the parent details")
class Child(Parent1,Parent2):
    def childDetails(self):
        print("these are the child details")

obj=Child()
obj.childDetails()
obj.parent1Details()
obj.parent2Details()
'''
what if Parent1 and Parent2 have same
function named test().
which copy will run when obj.test() called
and why ?
'''
