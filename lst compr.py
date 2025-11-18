#create a list with even numbers upto 200
L=[]
for i in range(2,201,2):
    L.append(i)
print("L:",L)
#List Comprehension is shortcut method for
#creating a list from given logic
#syntax -> name=[x for x in range()]
L2=[i for i in range(2,201,2)]
print("L2:",L2)
'''
create a list with even numbers upto 200
which are divisible by 5'''
L3=[v for v in range(2,201,2) if v%5==0]
print("L3:",L3)
