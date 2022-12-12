def add_two(a,b):
    return a+b
total = add_two(5,4)
print(total)

#printing directly

def add_two(a,b):
    return a+b
print(add_two(4,6))

#Inputing two numbers

def add_two(num1,num2):
    return num1+num2

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(add_two(a,b)) 

#Adding two strings

def name_string(f1,f2):
    return f1+" "+f2

first_name = input("ENTER FIRST NAME: ")
second_name = input("ENTER SECOND NAME: ")
print(name_string(first_name,second_name))


#Adding three numbers

def add_three(a,b,c):
    return a+b+c

print(add_three(3,6,8))  


#Last char of a name

def last_char(name):
    return name[-1]

print(last_char("serena sinha"))

#odd and even numbers using function

def odd_even(num):
    if num%2==0:
        return num
    else:
        return num

print(odd_even(19)) 





