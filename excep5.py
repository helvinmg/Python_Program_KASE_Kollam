#Exception handling
try:
    a=10
    b=5
    if a>b:
        raise KeyError("This is user defined exception")
        #raise Exception("This is user defined exception")
    else:
        print(a+b)
except Exception as e:
    print("Something went wrong")
    print(e.__class__.__name__)
    print(e)
else:
    print("All good no exception")
finally:
    print("I work always")
