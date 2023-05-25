# To concatinate 'Str' and 'int'

numbers = ["1", "2", "3"]
numbers = list(map(int, numbers))
numbers[2] += 1
print(numbers[2])


#Lambda in 'map

numbers = [1,2,3,4,5,6,7,8,9]
sq = list(map(lambda x:x*x, numbers))
print(sq)

# Alternate

def square(a):
    return a*a
num = [1,2,3,4,5,6,7,8,9]
sq = list(map(square, num))
print(sq)


# Square and Cube in lambda

def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square,cube]
num = [1,2,3,4,5]
for i in range(len(num)):
    val = list(map(lambda x:x(i), func))
    print(val)



#Filter

numbers = [1,2,3,4,5,6,7,8,9]
def is_greater(num):
    return num > 5
greater_then_5 = list(filter(is_greater, numbers))
print(greater_then_5)


# reduce
from functools import reduce


numbers = [1,2,3,4,5] #add all of these
num = reduce(lambda x,y:x+y, numbers)
print(num)

#Alternate
lis = [1,2,3,4]
num = 0
for i in lis:
    num += i
print(num)