#Exception handling
try:
    #print(4/0)
    d={'a':1}
    print(d['b'])
except Exception as e:
    print("im handling the exception")
    print(e)#display exception msg
finally:
    print("I work always")
