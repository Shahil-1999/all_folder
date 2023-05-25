class Employee:
    no_of_leaves = 9
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def All_details(self):
        return f"the name is{self.name}. Salary is {self.salary} and role is {self.role}"

x = Employee("Shahil", 456, "abc")
# print(x.salary)
print(x.All_details())

# The property of the constructor is that whenever we initialize an object of a class, the constructor gets automatically called.