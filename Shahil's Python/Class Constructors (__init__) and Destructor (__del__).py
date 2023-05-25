# in programming languages constructors are used to initialise the values
# constructor:-
class person:
    def __init__(self):  # this is constructor  (initializing the constructor, it always take double underscore){this self indicate to 'personName=person()'}
        print("Our class is Created")

    def setFullName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printFullName(self):
        print(self.firstName, " ", self.lastName)


personName = person()
personName.setFullName("shahil", "chourasia")
personName.printFullName()


# destructor:-

class person:
    def __init__(self):  # this is constructor  (initializing the constructor, it always take double underscore){this self indicate to 'personName=person()'}
        print("Our class is Created")

    def __del__(self):  # this is destructor,use to destroy the constructor always calls at very last
        print("our object is destroyed")

    def setFullName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printFullName(self):
        print(self.firstName, " ", self.lastName)


personName = person()
personName.setFullName("shahil", "chourasia")
personName.printFullName()
