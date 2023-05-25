def calculateGmean(a, b):
  mean = (a*b)/(a+b)
  print(mean)

def isGreater(a, b):
  if(a>b):
    print("First number is greater")
  else:
    print("Second number is greater or equal")

def isLesser(a, b):
  pass
  

a = 9
b = 8
isGreater(a, b)
calculateGmean(a, b)

c = 8
d = 74
isGreater(c, d)
calculateGmean(c, d)

# Function - A function is a block of code that performs a specific task whenever it is called.
# Built-in-function - These functions are defined and pre-coded in python.
# User Define Function - We can create functions to perform specific tasks as per our needs.