#SET operations
'''
1.Union
2.Intersection
3.Difference
4.Symmetric Difference
'''
S1={1,2,3,4,5}
S2={4,5,6,7,8}
print("Union",S1.union(S2))
print("Intersection",S1.intersection(S2))
print("Difference",S1.difference(S2))#S1-S2
print("Symmetric Difference")
print(S1.symmetric_difference(S2))
print("Union",S1|S2)
print("Intersection",S1&S2)
print("Difference",S1-S2)#S1-S2
print("Symmetric Difference",S1^S2)

