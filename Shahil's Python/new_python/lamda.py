


# def minus (x,y):
#     return x - y

# print(minus(10,5))


# # lamda
# minus1 = lambda a,b:a-b
# print(minus1(9,1))


# #  ex- 2
# a = [[1, 14], [5, 6], [8, 1]]
# a.sort(key=lambda a: a)  #only return sorted 1st index
# print(a)


from functools import *

a = [1,2,3,4,5,6,7,8,9]
r = list(filter(lambda x:x%2==0,a)) #filter is used for filter the list
print(r)
#I want to double even number
d = list(map(lambda x: x * 2, r))   # The map () function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
print(d)
#i want to add doubles for this wee need to import reduce from functools
add = reduce(lambda a,b:a+b,d)
print(add)





