L=[]
print(type(L))
fruits=["apple","banana"]
nums=[5,6,7,8]
mix=[5,"abc",6.7]
#same indexing (both forward & backward)
#same slicing as strings
#update a existing value
print(id(nums))
nums[0]=55
print(nums)
print(id(nums))
#add values 
nums.append(100)#single value
print("after appending",nums)
#add multiple values - list as arg
nums.extend([200,201])
print("after extending",nums)
#adding value at any index
nums.insert(2,70)#adding 70 at 2nd index
print("after inserting",nums)
#removing elements using index
delvalue=nums.pop()#remove the last element
nums.pop(2)#remove element from 2nd index
print("after pop",nums)
#removing elements using value
nums.remove(100)
print("after remove",nums)


