
#solution1
def square_list(l):
    square = []
    for i in l:
        square.append(i**2)
    return square
numbers=list(range(1,11))
print(square_list(numbers)) 

#Solution2
def reverse_list(l):
    l.reverse()
    return(l)

numbers=[1,2,3,4]
print(reverse_list(numbers))

#solution3
def reverse_words(l):
    elements=[]
    for i in l:
        elements.append(i[::-1])
        return elements
words = ['abc','vuw','xyz'] 
print(reverse_words(words)) 

#solution 4
def odd_even(l):
    odd_num=[]
    even_num=[]
    for i in l:
        if i%2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
        output=[odd_num,even_num]
        return output

elements=[1,2,3,4,5]
print(odd_even(elements))

#Solution 5
def greatest_diff(l):
    return max(l)-min(l)

numbers=[0,1,24,68,2]
print(greatest_diff(numbers))


