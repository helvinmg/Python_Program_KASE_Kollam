#sets
#unordered, does not allow duplicates
S1=set()
S2={3,4,5,"abc"}
print(S1, type(S1))
print(S2, type(S2))
S3={3,4,5,"abc",4,3,1,5}
print(S3)
S1.add(6)
S1.add(67)
S1.add(67)
print("S1 after addition",S1)
S1.remove(6)
print("S1 after removal",S1)
L=[1,2,3,2,4,5,1,6]
L=list(set(L))
print("L without duplicates",L)

