for i in range(0,11,2):
    print(i)

for i in range(1,-11,-1):
    print(i)


name = "Harshit"
for i in range(len(name)):
    print(name[i])


name = "Harshit"
for i in "Harshit":
    print(i)

total = 0
num = input("Enter a number: ")
for i in num:
    total+=int(i)
print(total)            
