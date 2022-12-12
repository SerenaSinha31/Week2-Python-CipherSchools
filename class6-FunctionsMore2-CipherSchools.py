#Functions inside a function
def greater(a,b):
    if a>b:
        return a
    else:
        return b

def greatest(a,b,c): 
    if a>b and a>c:
        return a 
    if b>a and b>c:
        return b
    else:
        return c

def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c) 

print((new_greatest(10,4,90)))                             