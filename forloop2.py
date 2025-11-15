#For Loop
'''
Syntax 1:
for value in range():
    body of the loop
'''
#range(start,stop) - stop will be stop-1
#default step is +1
print("range with start & stop")
for i in range(1,11):
    print(i)
print("range with only stop")
#range(stop) - first 0, last value 5
for i in range(6):
    print(i)
print("range with start,stop & step")
#range(start,stop,step)
for i in range(2,11,2):
    print(i)
