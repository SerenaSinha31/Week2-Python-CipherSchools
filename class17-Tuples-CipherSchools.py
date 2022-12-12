mixed = (1,2,3,4,0)
for i in mixed:
    print(i)


#tuple with one element
num=(1,)
print(type(num))

#tuple unpacking
guitarists=('abc','ptghfd','gdhdhd')
guitarist1, guitarist2, guitarist3 = (guitarists)
print(type(guitarists))

#list inside tuple
favourites = ('southern mangolia',['tokoyo','china'],'landscape')
favourites[1].pop()
favourites[1].append("WE made it")
print(favourites)

#something more about tuples
list,str
nums = tuple(range(1,11))
nums = list((1,2,3,4,5,6,7,8))
print(nums)
print(type(nums))

num_list=str([1,2,3,4,5,6,7,8])
print(num_list)
print(type(num_list))


