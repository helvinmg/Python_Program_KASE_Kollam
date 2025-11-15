users=["arun","varun","tharun","karan"]
searchname=input("enter the user name: ")
'''found=0
for name in users:
    if name==searchname:
        print("found user")
        found=1
        break
if found==0:
    print("user not found")'''
for name in users:
    if name==searchname:
        print("found user")
        found=1
        break
else:
    print("user not found ")
    
