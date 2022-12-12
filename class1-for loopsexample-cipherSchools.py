#sum of numbers
total=0
for i in range(1, 21):
     total+=i
print(total)

# sum of inputed number
num = int(input("Enter a number: "))
total=0
for i in range(1, num+1):
    total+=i
print(total) 

#ask a number from user and calculate its sum of digits
total = 0
num = input("Enter a number")
for i in range(0, len(num)):
    total+=int(num[i])
print(total)

#ask a user name and count each character
name = input("Enter the name")
temp=""
for i in  range (0, len(name)):
    if name[i] not in temp:
       print(f"{name[i]}:{name.count(name[i])}")
       temp+=name[i]

 #BREAK AND CONTINUE 

for i in range(1,11):
    if i==5:
        break
    print(i)


for i in range(1,11):
    if i==5:
        continue
    print(i)










