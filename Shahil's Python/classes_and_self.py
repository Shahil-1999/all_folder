# a class is an extensible programme code templet for creating object.
class person:   # person is the name of class
    def setFullName(self, firstName, lastName):     # whenever we define a function we use'def' keyword (self points to the class itself this is automatically take) self is first arguement firstName is a secont arguement lastName is a third arguement (whenever you define a member function in a classalways use 'self' as a first arguement and then give your rest of the arguement)
        self.firstName = firstName          # set the value of first name
        self.lastName = lastName            # set the value of second name, { . } dot is a separator ( upto this point we setting the first name and last name to the variable in a class)
    def printFullName(self):                # if your member function dosen't take any arguement you must pass atleast one arguement which is 'self'.
        print(self.firstName, " ", self.lastName)   # we assign first name after this " " space means we separate first and last name by space.
                                                    # upto this point defination of a class.
personName=person()  # personName is a object you also use whatever you want like a, b, c  ,(person is the name of class)
personName.setFullName("shahil", "chourasia")  #setFullName is a member function of a class  ( now this instance can call the member variable of the class.)
personName.printFullName()