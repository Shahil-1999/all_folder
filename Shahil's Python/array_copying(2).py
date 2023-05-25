from numpy import *
# Concatinate 2 arrays
arr8 = [1,2,3,4,5,6]
arr9 =[6,1,6,9,8,7]
print(concatenate([arr8,arr9]))


# Coppy an Array
arr10 = [1,2,3,4,5]
arr11 = arr10
print(arr10)
print(arr11) # Both array has the same address.
print(id(arr10))
print(id(arr11))	# Check array id


# Create 2 array at different location
arr12 = array([1,2,3,4,5])
arr13 = arr12.view()
print(arr12)
print(arr13) 
print(id(arr12))
print(id(arr13))



# Two type of Copying method, 1.Shallow method, 2.Deep Method

# Shallow Method
arr14 = array([1,2,3,4,5])

arr15 = arr14.view() # Values are changing for both array
arr14[1] = 7
print(arr14)
print(arr15)


# Deep copy 
arr14 = [1,2,3,4,5]
arr15 = arr14.copy() # any changes made to a copy of object do not reflect in original objects.
arr14[1] = 7
print(arr14)
print(arr15)
