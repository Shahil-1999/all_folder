# inheritance allows us to define a class in terms of another class, which make it easier to create and maintain an application.

class parent:
    value1 = ("This is value 1")  # this two variables are 'member variables'.
    value2 = ("This is value 2")

#i want to re use the variable which are there member variable which are there in parent class.
class child (parent):  # you just pass the name of a class from which you want to inherit.
    pass               # pass is just a place holder, it dosen't do anything. But suppose you don't want to implement your class and you want to leave your class as it is then pass will help you to avoid any error.

# whenever we want to make a child class instence example:-

parent1 = parent()   # we have created the instence of parents class
print(parent1.value1)   # we just want to print this parent1.value1
print(parent1.value2)   # we just want to print this parent1.value2
child1 = child()          # suppose child instance want to use value 1 and value 2
                        # i am inheriting from my parent class this value1 and value2 which are member variables of parent class is available to use from the intance of child class also because by inheritance we allowing the superclass which is 'parent class'from which are inheriting.
                        # the class from which we are inherriting (parent) is called superclass and the class which is inherriting (child) from superclassis called subclass.
print(child1.value1)
print(child1.value2)




class parent1:
    value1 = ("This is value 1")
    value2 = ("This is value 2")
class parent2:
    value3 = ("This is value 3")
    value4 = ("This is value 4")

class child (parent1, parent2):
    pass
parent1 = parent1()
print(parent1.value1)
print(parent1.value2)
print(parent2.value3)
print(parent2.value4)
child1 = child()
child2 = child()
print(child1.value1)
print(child1.value2)
print(child2.value3)
print(child2.value4)
