#Loop2
n=9
while n>=1:
    print(str(n)*n)
    n-=2

n=1
while n<=5:
    if n==1 or n==5:
        print(str(n)*6)
    else:
        print(n," "*6,n)
    n+=1
