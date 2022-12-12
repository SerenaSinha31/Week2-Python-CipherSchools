matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix[2])

matrix=[[1,2,3],[4,5,6],[7,8,9]]
for i in matrix:
    print(i)

numbers=list(range (1,11)) 
print(numbers)

popped_item=numbers.pop()
print(numbers)

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
        return negative
print(negative_list(numbers))        








