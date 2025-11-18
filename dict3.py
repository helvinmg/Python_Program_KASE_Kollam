d={'a':'apple','b':'banana','s':'strawberry'}
for key in d:
    print(key,d[key])
'''
keys(), values(), items()
'''
print(d.keys())
print(d.values())
print(d.items())
keys=list(d.keys())
items=list(d.items())
print("first key",keys[0])
print("first item",items[0])
