# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(myList)



# #i want to print only the value 4 to 7 from mylist
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[4:8]
# print(myList1) #it exclude 8, it only print upto 7



# #i want to print 5 to last
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[5:]
# print(myList1)
#alternate process
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[5:10]
# print(myList1)



# #if i want to print backward
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[-7:-1]
# print(myList1)



# #if i want to backward to last
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[-10:] #(-) jst put minus sign
# print(myList1)




# #if i want to print sum number
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[0::2] # this '2' means skip one value like it print '0' but skip '1' it print '2' but skip '3'
# print(myList1)



# #if i want to print odd number
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[1::2] # this '1' means the number start from 2nd position(1) and gapping is 2
# print(myList1)



# #if i want to skip 2 number and print every 3rd number
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[0:10:3] # this '3' means skip two value like it print '0' but skip ('1 and 2') it print '3' but skip ('4 and 5')
# print(myList1)
# #alternate
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[::3]
# print(myList1)



# #if i want to skip '1' value at a time in backward
# myList = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# myList1 = myList[::-2]  #it print'9', but skip '8', it print'7', but skip '6'
# print(myList1)



#slicing String
name = ('a','b','c','d')
name1 = name[2:3]
print(name1) #3rd value exclude
