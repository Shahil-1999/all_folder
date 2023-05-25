class Employee:
    no_of_leaves = 9
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    @staticmethod       #It can be called directly from a class but not through the instances of a class.
    def details(string):
        print("this is good boy", string)



x = Employee("Shahil", 456, "abc")
print("Salary is", x.salary)
print("number of leaves is", Employee.no_of_leaves)
x.details("abc")

