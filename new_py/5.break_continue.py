# Break = The break statement enables a program to skip over a part of the code. A break statement terminates the very loop it lies within.
# continue = The continue statement skips the rest of the loop statements and causes the next iteration to occur.


# # For loops Break


# for i in range(15):
#     print("5 x ",i, "=",5*i)
#     if (i == 10):
#         print("Break the table")
#         break


# # For loops Continue   

# for i in range(15):
#     if (i == 10):
#         print("Continue Statement is Executed")
#         continue
#     print("5 x ",i, "=",5*i)


# i = 0
# while True:
#   print(i)
#   i = i + 1
#   if(i % 10 == 0):
#     break


i = 10
while True:
  print(i)
  i = i + 1
  if(i % 2 == 0):
    break