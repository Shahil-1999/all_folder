# # display second highest number in the array
# def sort (c):
#     c.sort()
#     print("Second highest number is: ",c[len(c)-2])

# c = sort([1, 5, 98, 5, 25])


# a = "987654321"
# left=a[1:len(a):2]
# right=a[0:len(a):2]
# print(left+right)

# def sort (c):
#     c.sort()
#     return (c[0],c[len(c)-1])

# print(sort([1, 5, 98, 5, 25,101,0,-3]))

# def feb(a):
#     if (a == 0):
#         return 0
#     elif(a == 1):
#         return 1
#     else:
#         return feb(a - 2) + feb(a - 1)

# print(feb(5))



# Write a programe to remove the duplicate value nd find the second lowest and second heigest number. Note = input must be taken from user.

# def sol (a):
#     x = []
#     for i in a:
#         if i not in x:
#             x.append(i)
#             x.sort()
#     sh = x[len(x)-2]
#     l = x[1]
#     print (f"second lowest number is : {l}\nSecond highest number is : {sh}")


# a = list(map(int, input().split()))
# print(sol(a))



