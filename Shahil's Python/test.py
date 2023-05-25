
# # 2

# def OperationsBinaryString(str):
#     a=int(str[0])
#     i=1
#     while i<len(str):
#         if str[i]=='A':
#             a&=int(str[i+1])
#         elif str[i]=='B':
#             a|=int(str[i+1])
#         else:
#             a=int(str[i+1])
#         i+=2
#     return a

# str=input("Enter number(0,1) with A, B, C: ")
# print(OperationsBinaryString(str))
# # – A denotes AND operation
# #– B denotes OR operation
# #– C denotes XOR Operation'


# # 3

# def CheckPassword(s,n):
#     if n<4:
#         return 0
#     if s[0].isdigit():
#         return 0
#     cap=0
#     nu=0
#     for i in range(n):
#         if s[i]==' ' or s[i]=='/':
#             return 0
#         if s[i]>='A' and s[i]<='Z':
#             cap+=1
#         elif s[i].isdigit():
#             nu+=1

#     if cap>0 and nu>0:
#         return 1
#     else:
#         return 0

# s=input("Enter password: ")
# a=len(s)
# print(CheckPassword(s,a))


# # 4

# def findCount(n, arr, num, diff):
#     count=0
#     for i in range(n):
#         if(abs(arr[i]-num)<=diff):
#             count+=1

#     if count:
#         return count
#     return 0

# n=int(input())
# arr=list(map(int,input("Enter elements with space").split()))
# num=int(input())
# diff=int(input())
# print(findCount(n, arr, num, diff))


# #5
# n = int(input("Starting number: "))
# m = int(input("Ending number: "))
# sum1 = 0
# sum2 = 0
# for i in range(1,m+1):
#     if i % n == 0:
#         sum1+=i
#     else:
#         sum2+=i
# a=abs(sum2-sum1)
# print("Sum of numbers not divisible by ",n," - Sum of numbers divisible by ",n, " = ",a)


# # 7

# n = int(input("Enter array size"))
# sum1 = int(input("Enter that number to check how many number smaller then element"))
# arr = list(map(int, input("Enter element with space").split()))
# if n < 2:
#     print('-1')
# arr = sorted(arr)
# for i in range(n-1):
#     if arr[i] + arr[i+1] < sum1:
#         print("product",arr[i] * arr[i+1])
#         break
# else:
#     print('0')

# # 9

# a = input("Enter String")
# count = 0
# str1 = ""
# for i in a:
#     if i == '#':
#         count+=1
#     else:
#         str1+=i
# print("#"*count,str1)


# # 11
# def swap (user_input, str1, str2):

#     result = ''

#     if user_input != None:

#         result = user_input.replace(str1, '*').replace(str2, str1).replace('*', str2)

#         return result

#     return 'Null'

# user_input = input("Enter String : ")

# str1, str2 = map(str,input("Enter 2 alphabet from string which you want to wap(enter space between them)").split())

# print(swap(user_input, str1, str2))


# #14

# m = int(input("Starting value:"))
# n = int(input("Ending value:"))


# def calculate(m, n):
#     sum = 0
#     for i in range(m,n+1,1):
#         if i%3 == 0 and i%5 == 0:
#             print("The numbers divisible by both 3 and 5, between" ,m," and", n, " both inclusive are: ", i)
#             sum = sum + i
#     print("Sum of numbers divisible by both 3 and 5", sum)

# calculate(m,n)


# #16
# table_number = int(input("Enter Number: "))
# sum = 0
# for i in range(1, 11):
#     value = table_number * i
#     print(value, end=" ")
#     sum = sum + value

# print()
# print("sum is ", sum)


# a = int(input("array length"))
# arr = list(map(int,input("Input the elements(with space)").split()))
# arr.sort()
# print(arr)
# print(min(arr))
# print(max(arr))

# n = int(input("Enter no"))
# count = 0
# if n >= 0 and n <= 12:
#     for i in range(1, 7):
#         for j in range(1, 7):
#             if (i+j == n):
#                 count += 1
#     print(count)
# else:
#     print(0)


# samples= int(input("Enter samples: "))
# ranges = int(input("Enter range: "))
# count = 0
# final = []
# arr = list(map(int, input("Enter elements: ").split()))
# for i in range(0, ranges):
#     range1, range2 = [int(i) for i in input().split()]
#     for j in range(0, samples):
#         if range1 <= arr[j] <= range2:
#             count = count + 1
#     final.append(count)
#     count = 0
# for i in range(0, len(final)):
#     print(final[i], end=" ")


# def abc(m, n):
#     count = 0
#     for i in range(m,n+1):
#         if
#             print(i)
# m = int(input("enter m: "))
# n = int(input("enter n: "))
# abc(m,n)


# def rearrangeArray(arr, N):
# 	ind = None

# 	# Find index of 0
# 	for i in range(N):
# 		if (arr[i] == 0):
# 			ind = i
# 			break
# 	# Pivot the 0 element.
# 	j = -1
# 	temp = None
# 	for k in range(N):
# 		if (arr[k] < 0):
# 			j += 1

# 			# Don't swap with pivot.
# 			if (arr[j] == 0):
# 				j += 1

# 			temp = arr[j]
# 			arr[j] = arr[k]
# 			arr[k] = temp

# 	# swap the pivot with last negative.
# 	temp = arr[ind]
# 	arr[ind] = arr[j]
# 	arr[j] = temp

# 	for i in range(N):
# 		print(arr[i], end=" ")

# # Driver Code
# arr = [1, 0, -2, 3, 4, -5, -7, 9, -3]
# N = len(arr)

# rearrangeArray(arr, N)

# # This code is contributed by Saurabh Jaiswal


# a = int(input("Enter number: "))
# b = []
# for i in range (0, a):
# 	i+=1
# 	b.append(i)
# print(b)


# import numpy as np
# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# x = int(input("Enter number: "))
# y = int(input("Enter number: "))
# c = []
# d = np.square([a,b,x,y])
# c.append(d)
# print(c)

# def square(a):
#     return a*a

# def cube(a):
#     return a*a*a

# func = [square,cube]
# num = [1,2,3,4,5]
# for i in range(len(num)):
#     val = list(map(lambda x:x(i), func))
#     print(val)


# import math
# a = int(input("Enter number: "))
# # b = int(input("Enter number: "))
# print(math.sqrt(a))


# def cntElements(arr, n) :

# 	copy_arr = [0] * n

# 	for i in range(n):
# 		copy_arr[i] = arr[i]
# 	count = 0
# 	arr.sort()
# 	for i in range(n):
# 		if (arr[i] == copy_arr[i]) :
# 			count += 1

# 	return count

# # Driver code
# arr = list(map(int,input().split()))
# n = len(arr)

# print(cntElements(arr, n))


# # Function for nth Fibonacci number
# def Fibonacci(n):

# 	# Check if input is 0 then it will
# 	# print incorrect input
# 	if n < 0:
# 		print("Incorrect input")

# 	# Check if n is 0
# 	# then it will return 0
# 	elif n == 0:
# 		return 0

# 	# Check if n is 1,2
# 	# it will return 1
# 	elif n == 1 or n == 2:
# 		return 1

# 	else:
# 		return Fibonacci(n-1) + Fibonacci(n-2)

# # Driver Program
# print(Fibonacci(7))


# #Same elements print
# a = list(map(int, input("elements: ").split()))
# b = list(map(int, input("elements: ").split()))
# c = []

# for i in range(len(a)):
#     for j in range(len(b)):
#         if a[i] == b[j]:
#             c.append(a[i])
# print(c)


# # Remove duplicate items
# n=int(input())
# arr=list(map(int,input().split()))
# dup=[]
# for i in arr:
#     if(i not in dup):
#         dup.append(i)
# print(dup)


# x = int(input("Enter How many dealers: "))
# for i in range(x):
#     cars = int(input("Enter How many cars: "))
#     bikes = int(input("Enter how many bikes: "))
#     cars_tyre = cars * 4
#     bikes_tyres = bikes * 2
#     print(f"total cars tyre {cars_tyre}, total bikes tyre{bikes_tyres}")
#     print("overall tyres: ", cars_tyre + bikes_tyres)


# alternate

# x = int(input("Enter how many dealer: "))
# for i in range(x):
#     cars, bikes = map(int,input("Enter how many cars: ").split())

#     cars_tyre = cars * 4
#     bike_tyre = bikes * 2
#     print("total cars tyre", cars_tyre)
#     print("total bikes tyre: ", bike_tyre)
#     print("Total tyres", cars_tyre + bike_tyre)


# n=int(input())
# arr=list(map(int,input().split()))
# dup=[]
# for i in arr:
#     if(i not in dup):
#         dup.append(i)
#         print("{} occurs {} times".format(i,arr.count(i)))


# def sum(n):
#     if(n==0):
#         return 0
#     return n+sum(n-1)

# sum(5)


# x = int(input("Enter "))
# for i in range(x):
#     a,b,c = map(int,input("elements ").split())
#     a = a*4
#     b = b * 2
#     c = c*0
#     print(a+b+c)


# a = "abbbbccc"
# x = {}
# count = 0
# for i in a:
#     if i in x:
#         x[i]+=1
#     else:
#         x[i]=1

# result = max(x, key=x.get)
# print(result)


## n+(n-1) + n+(n-1)

# a = int(input("Enter"))

# y = 0
# for i in range(1,a+1):
#     y += a+(a-i)
# print(y)


##n*(n-1) + n*(n-1)
# a = int(input("Enter Number: "))
# sum = 0

# for i in range (1, a+1):
#     x = a*(a-i)
#     sum = sum + x
# print(sum)


# def feb(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return feb(n-2) + feb(n-1)
# n = int(input("Enter no: "))
# print(feb(n))


# def integer(m, num):
#     r = num % m
#     if (r < (m+1)/2):
#         return num-r
#     else:
#         return num+(m-r)

# m = int(input("Enter number"))
# num = int(input("Enter number"))
# print(integer(m,num))


# def encodedChar(str, k):

#     expand = ""

#     freq = 0

#     i = 0

#     while(i < len(str)):

#         temp = ""

#         freq = 0

#         while (i < len(str) and

#                ord(str[i]) >= ord('a') and

#                ord(str[i]) <= ord('z')):
#             temp += str[i]

#             i += 1
#         while (i < len(str) and

#                ord(str[i]) >= ord('1') and

#                ord(str[i]) <= ord('9')):

#             freq = freq * 10 + ord(str[i]) - ord('0')

#             i += 1

#         for j in range(1, freq + 1, 1):

#             expand += temp
#     if (freq == 0):

#         expand += temp
#     return expand[k - 1]


# if __name__ == '__main__':

#     str = "ab4c12ed3"

#     k = 21

#     print(encodedChar(str, k))


# def module(num):
#     r = num%11
#     if r:
#         return r
#     else:
#         return 0


# num = int(input())
# print(module(num))


# n = int(input("Enter Number: "))

# for i in range(1, 11):
# 	q = n*i

# print(n, "x",i,"=",q)


# m1=int(input("Enter price: "))
# m2=int(input("Enter price: "))
# m3=int(input("Enter price: "))
# m4=int(input("Enter price: "))


# total = m1+m2+m3+m4

# costdis=0.0
# if total <= 25000:
# 	pass

# elif total > 25001 and total < 50000:
# 	costdis = total*5/100
# elif total > 50001 and total < 100000:
# 	costdis = total*7/100
# elif total > 100001:
# 	costdis = total*10/100


# metdis = m1*0.07 + m2*0.03 + m3*0.02 + m4*0.01


# if costdis > metdis:
# 	print(costdis)
# else:
# 	print(metdis)


# a = str(input("Enter name: "))
# b=0
# for i in range (len(a)):
# 	b+=1
# print(b)


# name = input("Enter name : ")
# reverse = name[::-1]
# if name == reverse:
# 	print("String is palindrome")
# else:
# 	print("String is not palindrome")


# import sqlite3


# def create(id, f_name, l_name, city, code ):


# 	conn = sqlite3.connect('INSTRUCTOR.db')

	
# # Before creating a table, let's first if the table already exist or not. To drop the table from a database use DROP query. A cursor is an object which helps to execute the query and fetch the records from the database.
# # Drop the table if already exists.
# 	cursor_obj = conn.cursor()
# 	cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")

# # Creating table
# 	table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, f_name VARCHAR(20), l_name VARCHAR(20), city VARCHAR(20), code CHAR(2));"""
# 	cursor_obj.execute(table)
# 	print("Table is Ready")

# # We will start by inserting just the first row of data, i.e. for instructor Rav Ahuja
# 	cursor_obj.execute("insert into INSTRUCTOR (id, f_name, l_name, city, code) values(?,?,?,?,?)",
#                    (id, f_name, l_name, city, code))
# 	cursor_obj.execute(
#     '''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')
# 	statement = '''SELECT * FROM INSTRUCTOR'''
# 	cursor_obj.execute(statement)
# 	print("All the data")

# # In this step we will retrieve data we inserted into the INSTRUCTOR table.
# 	output_all = cursor_obj.fetchall()
# 	for row_all in output_all:
# 		print(row_all)

# # Fetch few rows from the table
# 	statement = '''SELECT * FROM INSTRUCTOR'''
# 	cursor_obj.execute(statement)
# 	print("All the data")

# # If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
# 	output_many = cursor_obj.fetchmany(2)
# 	for row_many in output_many:
# 		print(row_many)


# # Fetch only FNAME from the table
# 	statement = '''SELECT FNAME FROM INSTRUCTOR'''
# 	cursor_obj.execute(statement)
# 	print("All the data")

# # In this step we will retrieve only name data.
# 	output_column = cursor_obj.fetchall()
# 	for fetch in output_column:
# 		print(fetch)



# def hcf(x,y):

# 	if x>y:
# 		smaller = y
# 	else:
# 		smaller = x
# 	for i in range(1, smaller+1):
# 		if((x%i==0) and (y%i==0)):
# 			hfc = i
# 	return hfc

# x = int(input("Enter First number: "))
# y = int(input("Enter First number: "))
# z = hcf(x,y)
# print(z)



# def DecimalToBinary(num):
# 	if num >= 1:
# 		DecimalToBinary(num // 2)
# 	print(num % 2, end = '')

# dec_val = 24
# DecimalToBinary(dec_val)


# def feb(n):
# 	if n == 1:
# 		return 0
# 	elif (n==2):
# 		return 1
# 	else:
# 		return (feb(n-2)+feb(n-1))

# n = int(input("Enter number:"))
# print(feb(n))




# prime check

# def isPrime(n):

#     # Check from 2 to n-1
#     for i in range(2, n):
#         if n % i == 0:
#             return 'not prime'

#     return 'prime'

# n = int(input("Enter number: "))
# print(isPrime(n))



# # prime number
# number = int(input("Enter the input Range : "))
# for i in range(2,number+1):
# 	for j in range(2,i):
# 		if (i % j) == 0:
# 			break
# 	else:
# 		print(i)



# number divisible by whome
# number = int(input("Enter the input Range : "))
# for i in range(1,number):
# 	if (number%i) == 0:

# 		print(i)


# gcd
# import math
# a = int(input("Enter first"))
# b = int(input("Enter second"))
# c = math.gcd(a, b)
# print(c)







n = 5
for i in range(1, n+1):
    for k in range(1, i+1):
        print("*", end="")
    print()