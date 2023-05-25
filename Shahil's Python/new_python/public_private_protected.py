class Employee:
    no_of_leaves = 9    #this is public variable
    _protected= 18  # this is protected variable u can only use main class and its subclass, u can not access by another class
    __private = 50 # this is private variable u can only use in main class, no child or ther class
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def All_details(self):
        return f"the name is{self.name}. Salary is {self.salary} and role is {self.role}"

class Programmer(Employee):
    def __init__(self, aname, asalary, arole,alanguages):   #This is not recomended to add new parameter with old class, because it will breake code reuseablity concept.
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguages

    def PrintProg(self):
        return f"The Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role}address is {self.language}."

class coolProg():
    languages = "cpp"
    def lang(self):
        print(self.languages)



x = Employee("Shahil", 456, "abc")

# print(x.salary)
# print(x.All_details())

# x.ChangeLeaves(20)
# print(x.no_of_leaves)
# print(y.All_details())
r = Programmer("rohan",455,"programmer",["python", "HTML", "CSS"])
# print(r.PrintProg())
print(x._protected)
q = coolProg()
print(q._protected) #It will throw an error bacause we try to access protected variable from another class.
print(x._Employee__private) #This is namning convention first u have to write "_class name" where ur private variable present and after that u will write "__private variable name" this is called mangling"
print(r._Employee__private)