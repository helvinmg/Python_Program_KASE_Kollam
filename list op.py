marks=[41,35,36,47]
marks2=marks#just reference is copied
marks2[0]=40#update in same memory loc
print(marks)
#we need use copy function to make copies
marks3=marks.copy()
marks3[0]=30
print("after updating marks3")
print("marks: ",marks)
print("marks3: ",marks3)
print("marks",id(marks))
print("marks2",id(marks2))
print("marks3",id(marks3))
