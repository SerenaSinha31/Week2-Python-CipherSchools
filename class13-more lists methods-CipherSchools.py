#in keyword
fruits=['grapes', 'Appples', 'Mango']
if 'Mango' in fruits:
    print("Mango is present")
else:
    print("Mango is not present")

#Some more list methods
fruits1=['grapes', 'Appples', 'Mango']  
print(fruits.count('grapes'))
fruits1.sort()
print(sorted(fruits1))

fruits1.clear()
print(fruits1)

#split and join method
#Convert string to list
user_info='Serena,24'.split(',')
print(user_info)

name,age='Serena,24'.split(',')
print(name)
print(age)





