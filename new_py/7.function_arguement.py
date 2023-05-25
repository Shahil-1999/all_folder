# Default Arguement - We can provide a default value while creating a function. This way the function assumes a default value even if a value is not provided in the function call for that argument.

def name(fname, mname = "Jhon", lname = "Whatson"):
    print("Hello,", fname, mname, lname)

print(name("Amy"))

# Keyword Arguement - We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

print(name(mname = "Peter", lname = "Wesker", fname = "Jade"))

# Required Arguement - In case we don’t pass the arguments with a key = value syntax, then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.

def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name("Peter", "Quill")
