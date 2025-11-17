n=int(input("how many values in the list"))
lst=[]
for i in range(n):
    value=int(input(f"Enter the value {i+1}:"))
    lst.append(value)
print("The list created is",lst)
'''
s="abcd"
for i in s:
    lst.append(i)
print("The list created is",lst)
'''
for ele in lst:
    if ele%5==0:
        lst.remove(ele)
        
print("updated list",lst)
print("sum of updated list",sum(lst))
