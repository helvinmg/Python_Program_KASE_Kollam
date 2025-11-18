#Dictionary - Mapping Type
#Unordered, No Index, Access using keys
#{key:vaulue}
#keys are unique and of immutable type
d1={}
d2=dict()
print(d1,d2)
d3={"a":1,"b":2,"c":3}
print(d3)
stud={101:"arun",102:"amal"}
print(stud)
dd={1:"apple","two":False,4.5:"random"}
print(dd)
#access
print("d3['a']:",d3["a"])
print("stud[101]",stud[101])
#update
stud[101]="arjun"
print("stud[101]",stud[101])
#del
del stud[101]
print("after deletion",stud)
#adding new key:value pair
stud[103]="varun"
stud[104]="karan"
print("after adding",stud)
