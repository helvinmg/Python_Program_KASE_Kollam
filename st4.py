'''
Reverse a string without using built-in functions
or string slicing '''
st="elephant"
rev=""
for i in range(len(st)-1,-1,-1):
    rev=rev+st[i]
print(rev)
