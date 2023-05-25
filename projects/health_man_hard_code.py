# Health Management System
# 3 clients - shahil, shiwani and biswarup

# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if(c == 1):
            value = input("type here\n")
            with open("shahil-ex.txt", "a") as op:
                op.write(str() + value+"\n")
            print("successfully written")
        elif(c == 2):
            value = input("type here\n")
            with open("shahil-food.txt", "a") as op:
                op.write(str() + value + "\n")
            print("successfully written")
    elif(k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("shiwani-ex.txt", "a") as op:
                op.write(str() + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("shiwani-food.txt", "a") as op:
                op.write(str() + value + "\n")
            print("successfully written")
    elif(k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("biswarup-ex.txt", "a") as op:
                op.write(str() + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("biswarup-food.txt", "a") as op:
                op.write(str() + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(shahil),2(shiwani),3(biswarup)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if(c == 1):
            with open("shahil-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif(c == 2):
            with open("shahil-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("shiwani-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("shiwani-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif(k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("biswarup-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("biswarup-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (shahil,shiwani,biswarup)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for shahil 2 for shiwani 3 for biswarup "))
    take(b)
elif a == 2:
    b = int(input("Press 1 for shahil 2 for shiwani 3 for biswarup "))
    retrieve(b)
else:
    print("please enter valid input")











