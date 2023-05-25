class Employee:
    no_of_leaves = 9
    pass

shahil = Employee()
manish = Employee()

shahil.name = "shahil"
shahil.sal = 4554
manish.name = "manish"
manish.sal = 45

print(Employee.no_of_leaves) # you can access no of leaves by shahil,manis, employee anything
print(manish.no_of_leaves)
print(shahil.no_of_leaves)


#You want to change the value of class employee then you have only one option 
Employee.no_of_leaves = 10
print(Employee.no_of_leaves)