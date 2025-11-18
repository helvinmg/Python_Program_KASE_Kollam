#Exception handling
try:
    print(b)
except ZeroDivisionError:
    print("Handling Division By Zero")
except Exception as e:
    print("im handling the exception")
    print(e)
finally:
    print("I work always")
