#python does not allow multiple defintions for a
#single function unlike java
a=10
a=20
def test(value):
    print("test with value",value)
def test():
    print("simple test")

test()#latest function definition will be considered
