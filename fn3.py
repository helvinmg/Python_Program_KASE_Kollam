#default parameter/arguments
def findlarge(a,b,c=0):
    if a>b and a>c:
        return f"largest is a {a}"
    elif b>a and b>c:
        return f"largest is b {b}"
    else:
        return f"largest is c {c}"

lg=findlarge(10,30,61)
print("Largest is",lg)

