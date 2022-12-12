def greater(a,b):
    if a>b:
        return a
    if b>a:
        return b
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(greater(num1,num2))

#find greatest of three functions
def greatest(a,b,c):
    if a>b and a>c:
        return a
    if b>a and b>c:
        return b
    else:
        return c

print(greatest(2,5,6))

