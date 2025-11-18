#Exception handling
try:
    print("hello",b)
except Exception as e:
    print("Something went wrong")
else:
    print("All good no exception")
finally:
    print("I work always")
