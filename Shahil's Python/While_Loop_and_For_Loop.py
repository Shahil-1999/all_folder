# WHILE LOOP

a = 0
while a<10:
    print(a)
    a+=1  # Increase 1 (Alternate code is a=a+1)



a = 1
sum = 0
print("Enter number to add to the sum")
while a!= 0:
    print("current sum",sum)
    print("Enter 0 to quit")
    a = float(input("Number:"))  # Float means integer and Decimal values both accept (if i write 'int' in place of float then it takes only integer part not decimal
    a = float(a)        # if here i write 'int' in place of float it converts in round figure
    sum += a   # S add in 'a' then 'a' then 'a' and so on
print("total sum=", sum)



num = 1        # if we have provided initial value of 'num = 0' then while condition will never be ment all while statement never be executed
sum = 0
print("Enter a number. Please Enter 0 to Exit")

while num != 0:     # num should not be equal to '0' then only all code will be executed
    num = float(input("Enter Numbrr:"))     # this 'num' will be assign to the 'variable num' variable num 'line 21'    #whenever user provide the value 'num = 1' be overwritten by the value which is provided by the user.
    sum = sum + num
    print("Total", sum)


# FOR LOOP

a = [1,8,9,6,2,5,4,7,8,2,6,2,4]  # If i want to print these number one by one
for number in a:   # "number" is just a variable you take variable what you want according to you this is not mandatory
    print(number)


a = [0, 1, 2, 3, 4, 5]      # List
b = (0, 1, 2, 3, 4, 5)      # Tuples
c = {0, 1, 2, 3, 4, 5}      # Sets
d = '12345'                 # Strings
e = {"Name": 'Shahil', "roll": '47'} # Dictionary
print(0 in a)       # 'in' operator will give you 'true' or 'false' depending upon weather 'o' is present in your sequence or not
print(50 in a)
print(1 in b)
print(60 in b)
print(1 in c)
print(60 in c)
print('1' in d)
print('60' in d)

for y in a:
    print(y)

for y in b:
    print(y)

for y in c:
    print(y)

for y in d:
    print(y)

for y in e.items:
    print(y)

for y, z in e.items():      # in ditionary
    print(y, " ", z)



for x in range(2, 30, 3):   # '2' is starting value, '30' is last value but it print upto 29, '3' is step
    print(x)
else:
    print("Finished")

