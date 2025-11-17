#Nested List
import copy
NL=[1,[7,9],3,4,[1,2,3]]
#     0    1    2 3     4
print(NL)
print(NL[1])#[7,9]
print(NL[1][1])#9
NL2=NL.copy()#shallow copy
NL3=copy.deepcopy(NL)#deepcopy
NL[0]=10
print("after update:  NL",NL)
print("after update: NL2",NL2)
print("after update: NL3",NL3)
NL[1][1]=90
print("after update:  NL",NL)
print("after update: NL2",NL2)
print("after update: NL3",NL3)


