s="abcde"
'''
creating dict with ind as key and ele as value
d={0:a,1:b,2:c,3:d,4:e}
'''
#method1
'''
d1={}
for ch in s:
    d1[s.index(ch)]=ch
print(d1)
'''
#method2
d2={}
for i in range(0,len(s)):
    d2[i]=s[i]
print(d2)
