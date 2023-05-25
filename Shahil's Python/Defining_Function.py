# a function is a group of statements that together perform a specific task
# how we can define a function.
def functionname (arg1, arg2): # def is a KEYWORD,  and in 'functionname' you write what you print many time like say to hello to 100 people and 'arg' means argument there is no limit of argument.
    Statement1  # Statement are the piece of code which you write inside a function.
    Statement2


# i want to print hello to 100 people and i dont want to rewrite print("hello...") again and again
def hello(name):  # (name = variable )
    print("hello ", name)  # this is statement and you must insert double enter


hello("shahil")
hello("john")
hello("shiwani")



def add(x,y):
    return (x+y)    # return means result.


sum1 = add(10, 20)  #10 is assign to "x" and 20 is assign to "y"
print(sum1)
sum2 = add(22.2,73.2)
print(sum2)