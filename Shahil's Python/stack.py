


stack = []

def push():
    if len(stack) == n:
        print("Stack is full")
    else:
        elements = input("Enter Elements: ")
        stack.append(elements)
        print(stack)

def pop():
    if not stack:
        print("Stack is empty")
    else:
        e = stack.pop()
        print("Element remove: ",e)
        print(stack)

n = int(input("Enter Limit of stack: "))
while True:
    print("Select the option 1.Push 2.Pop 3.Quit")
    choose = int(input("Enter Option: "))
    if choose == 1:
        push()
    elif choose == 2:
        pop()
    elif choose == 3:
        break
    else:
        print("Please Choose valid Option")


# import numpy as np


# stack = []

# def push():
#     if len(stack) == n:
#         print("Stack is full")
#     else:
#         x = list(map(int,input("Enter Elements: ").split()))
#         c = np.array(x)
#         d = c.flatten()
#         stack.append(d)
#         print(stack)

# def pop():
#     if not stack:
#         print("Stack is empty")
#     else:
#         e = stack.pop()
#         print("Element remove: ",e)
#         print(stack)



# n = int(input("Enter Limit of stack: "))
# while True:
#     print("Select the option 1.Push 2.Pop 3. Quit")
#     choose = int(input("Enter option: "))
#     if choose == 1:
#         push()
#     elif choose == 2:
#         pop()
#     elif choose == 3:
#         break
#     else:
#         print("Please Choose valid Option")

