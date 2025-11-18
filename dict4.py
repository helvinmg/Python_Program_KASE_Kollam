#functions for dict manipulation
#1. syntax: dict1.update(dict2)
stud_list1={10:"arun",20:"varun"}
stud_list2={30:"mahesh",10:"vishnu"}
stud_list1.update(stud_list2)
#add the items of list2 to list1
print("updated list1",stud_list1)
#2. syntax: dict.pop(key)
deleted=stud_list1.pop(10)
print("after pop",stud_list1)
print("popped value",deleted)
#3. syntax: dict.popitem() - removes last
#inserted key-value pair
stud_list1.popitem()
print("after popitem",stud_list1)
#4.  syntax: dict.clear() - removes all items
stud_list1.clear()
print("after clear",stud_list1)
