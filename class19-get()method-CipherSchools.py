d = {"name":"unknown","age":"unknown"}
print(d.get("name"))

if d.get("name"):
    print("present")
else:
    print("not present")

#clear
#d.clear()
#print(d)

#copy
d1 = d.copy()

d1=d
print(d1.popitem())
print(d)

user={'name':'Harshit','age':'24'}
print(user.get('name','not found!'))

#one dictionary can have only one key

user={'name':'Harshit','age':'24','age':'24'}
print(user)

#more get()


