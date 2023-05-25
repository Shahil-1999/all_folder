def student(names, age):
    print("name:", names)
    print("age:", age)

student("max", 22)




# Default Values
def student(names ="Unknown Name", age = 0):   # If somebody desent provide any name or age then print 'Unknown Name', 0.
    print("name:", names)
    print("age:", age)

student()
#Default values are used when u want to make sure that every arguement in your function should have some value.



def student(names ="Unknown Name", age = 0):
    print("name:", names)
    print("age:", age)

student("tom")  # I just provide a name here and dont provide any age, then you can see the name is overwritten by the arguements what we have provided here.




#Variable length arguements
# I want to provide the list of scores which this students has scored for different subjects.

def student(names, age, *marks):    #you can use '*' astricks in front of your arguements and this means thgat you can provide multiple arguement when you use this kind of notation.
    print("name:", names)
    print("age:", age)
    print("marks:", marks)

student("tom", 22, 80, 65, 89)
#Whenever u provide '*' this astricks in front of the arguement u can provide some values for that arguement.




#use of for loop in order to itrate aver tuples.
def student(names, age, *marks):
    print("name:", names)
    print("age:", age)
    for x in marks:
        print(x)    #for loop has printed all these marks which are there inside the list.

student("tom", 22, 80, 65, 89)




#Double astricks (marks and subjects)
def student(names, age, **marks):
    print("name:", names)
    print("age:", age)
    print("marks", marks)

student("tom", 22, math = 22, physics = 80, Biology = 65, Hindi = 89)
#When u use double astricks in front of ur arguement u can provide these kind of key value pairs which are seprated by this '=' symbol.
#Whenever u use double astricks the values are given to u in the form of a dictionery.




def student(names, age, *marks):
    print("name:", names)
    print("age:", age)
    print("marks", marks)
    for x in marks:
        print(x)    #only keys are printed and not the values of these subjects are printed.

student("tom", 22, math = 22, physics = 80, Biology = 65, Hindi = 89)




#printed keys and their values
def student(names, age, **marks):
    print("name:", names)
    print("age:", age)
    for key,value in marks.items():
        print(key, ' ', value)
student("tom", 22, math = 22, physics = 80, Biology = 65, Hindi = 89)