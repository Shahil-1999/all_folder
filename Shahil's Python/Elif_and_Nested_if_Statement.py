# name = input("Name:")
# if name == "mark":  #that(==) means you compare Two values
#     print("the name entered is",name)
# elif name == "john":   #elif means to check multiple condition
#     print("the name entered is",name)
# elif name =="wick":
#     print("the name entered is",name)
# else:
#     print("the name entered is Invalid")



#i want to have multiple "if" condition inside "if" condition its called "nested if" condition
name = "animal"
animalName = "dog"
if name=="animal":   #this is like a parent "if"
    if animalName =="dog":          # this is like a child "if"( this is "nested if" condition
        print("valid animal")
    else:
        print("invalid animalName")
    print("name entered is animal")
else:
    print("the name entered is not valid")

    