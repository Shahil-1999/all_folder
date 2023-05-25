class Employee:
    no_of_leaves = 9
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def All_details(self):
        return f"the name is{self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def ChangeLeaves(cls, newleaves):
        cls.no_of_leaves = newleaves
    
    @classmethod
    def dash(cls, string):
        # z = string.split("-")
        # return cls(z[0],z[1],z[2])

    # alternate of split
        return cls(*string.split("-"))

class Programmer(Employee):
    def __init__(self, aname, asalary, arole,alanguages):   #This is not recomended to add new parameter with old class, because it will breake code reuseablity concept.
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.language = alanguages

    def PrintProg(self):
        return f"The Programmer's name is {self.name}. Salary is {self.salary} and role is {self.role}address is {self.language}."



x = Employee("Shahil", 456, "abc")
y = Employee.dash(" shahil-4566-fdge")
# # print(x.salary)
# print(x.All_details())

# x.ChangeLeaves(20)
# print(x.no_of_leaves)
# print(y.All_details())
r = Programmer("rohan",455,"programmer",["python", "HTML", "CSS"])
# print(r.PrintProg())
