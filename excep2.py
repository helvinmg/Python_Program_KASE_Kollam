#Exception handling
try:
    print("hello",b)
except Exception as e:
    print("im handling the exception")
    print(e)
finally:
    print("I work always")
