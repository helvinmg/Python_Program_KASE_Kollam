def test():
    global x
    x=10
    print("inside fn",x)

test()
print("outside fn",x)
