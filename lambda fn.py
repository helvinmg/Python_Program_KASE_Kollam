#Lamda Function
#lambda arguments:statement/return
findsum=lambda x,y:x+y
res=findsum(5,6)
print(res)

hello=lambda name: print(f"hello {name}")
hello("manu")

L=[2,3,4]
#map(fn,seq)
res=map(lambda x:x*2,L)
print(list(res))#map returns object
