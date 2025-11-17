#String Slicing
#st[start:stop:step]
s="abcdefghijklmn"
print(s)
#same logic as range - step is +1 by default
#start is 0 by default
print("s[0:5]",s[0:5])#start,stop
print("s[0:5:2]",s[0:5:2])#start,stop,step
print("s[10:0]",s[10:0])
print("s[10:0:-1]",s[10:0:-1])
#special cases
print("s[:5]",s[:5])
print("s[5:]",s[5:])#it will take till eof string
print("s[::2]",s[::2])#step is 2, start=0, stop=eof
print("s[::-1]",s[::-1])#start=len-1, stop=-1
#s[13:-1:-1]
