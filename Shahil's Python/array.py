# arr = []
# n = int(input("Enter the length of array: "))
# for i in range (n):
# 	x = int(input("Enter elements: "))
# 	arr.append(x)
# 	arr.sort()
	
# print(arr)

# # Mannually
# val = int(input("Enter elements which you want to search: "))
# k = 0 	# for index
# for e in arr:   # here e means value present in array
# 	if e == val:
# 		print("Index number is: ", k)
# 		break
# 	k+=1


# # By built in function
# val = int(input("Enter elements which you want to search: "))
# print("Index is : ",arr.index(val))




from numpy import *
# # array()
# arr = np.array([[1,2,3],[4,5,6]])

# arr2 = np.array([4,5,6.1], int) # I want to take float into int

# print(arr)
# print(arr2)


# # Linspace()
# arr3 = np.linspace(1,90,20)
# print(arr3) # It provide us 1 to 90 equally spaced 20 elements


# # Arange()
# arr4 = np.arange(1,20,3)
# print(arr4) # It provide 1 to 20 and skip 3 values


# #Logspace()
# arr5 = np.logspace(1,40,5)
# print(arr5) # the no. of parts would be 5 so these spacing b/n two numbers would be depend upon the log of it. it will start from 10 raised to 1 to 10 raised 40 and it will get divided into 5 parts.


# #zeros
# arr6 = np.zeros(5)
# print(arr6) # It will create an array of size 5 with all the no. of zeros.


# # Ones
# arr7 = np.ones(5)
# print(arr7) # It will create an array of size 5 with all the no. of Ones.



