


class Employee:
    no_of_leaves = 9
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def All_details(self):
        return f"the name is{self.name}. Salary is {self.salary} and role is {self.role}"

class player:
    no_of_leaves = 10
    def __init__(self, name, game):
        self.name = name
        self.game = game
    def printDetails(self):
        return f"Player name is {self.name} and that player plays {self.game}"

class coolProg(Employee,player):
    languages = "cpp"
    def lang(self):
        print(self.languages)


z = coolProg
print(z.no_of_leaves)


