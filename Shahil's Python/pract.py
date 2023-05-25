'''
a=input("Enter the Username:")
print(a)
b=input("Enter the Password:")
print(b)
c=len(b)
if (c>=8)and(c<=16):
    print("Password is valid")
else:
    print("password is Invalid")
if  ('A-Z'[0]) in b:
    print("Password is valid")
else:
    print("Password is Invalid")
if ' ' in b:
    print("Password is Inalid")
else:
    print("Password is valid")
if '0-9' in b:
    print("Password is valid")
else:
    print("Password is invalid")
if '!@#$%&*' in b:
    print("Password is valid")
else:
    print("Password is invalid")
if a in b:
    print("username should not present in password")
else:
    print("continue to login")
    '''

# no_rows = int(input("Enter rows: "))
# for row in range (1, no_rows):
#     for column in range (1, row + 1):
#         print("*", end=" ")
#     print()

# for row in range (no_rows, 0, -1):
#     for column in range (1, row + 1):
#         print("*", end=" ")
#     print()


# no_rows = int(input("Enter rows: "))
# for row in range (1, no_rows + 1):
#     # Display spaces
#     for space in range (1, (no_rows - row) + 1):
#         print(" ", end = "")

#     #Display Symbol
#     for symbol in range (1, row + 1):
#         print("*", end=" ")
#     print()

