#special arguments - dynamic arguments
#python allows us to pass any number of arguments
def splsum(*nums):
    print("I received",nums)
    sum=0
    for i in nums:
        sum=sum+i
    print("sum is",sum)
