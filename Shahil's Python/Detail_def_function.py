#Functions = function is a group of statements within a programe that performs a specific task.
#Types of function = built-in-function, user define function.
#Built-in-function = print, input, min, max, etc....


def nameoffunction (arg1, arg2):
    print(" ") # under this function signature u write some statement which u want to execute when this function is called


def sum (arg1, arg2):
    print(arg1 + arg2)
sum(15, 5) #call the function = in order to call a function u jst used to name of the function and then you provide the arguement which is required by the function.





def sum (arg1, arg2):
    print(arg1 + arg2)  # this + operator u can also use to concatinate to string.
sum('Hello', 'World')





def sum (arg1, arg2):
    if type(arg1) != type(arg2):
        print("Please give the arguement of same type")
        return  #return keyword is used to return something, when u write this return function without any value here its going to return nothing but as soon as this return keyword is called nothing after that will be executed.
    print(arg1 + arg2)
sum("Hello", 5)





def sum (arg1, arg2):
    if type(arg1) != type(arg2):
        print("Please give the arguement of same type")
        return
    return (arg1 + arg2) 
sum(4, 5)
sum("hello", "world")
sum("Hello", 5)
# All sum is executed but the result is not printed so in order to get result out of this function when it return something we need to save this return value in a variable.






def sum (arg1, arg2):
    if type(arg1) != type(arg2):
        print("Please give the arguement of same type")
        return
    return (arg1 + arg2) 
a = sum(4,5)
print(a)
print(sum("hello", "world")) # you can directly enclosed this sum function inside a print function and then also its going to print the sum of these two string.
print(sum("Hello", 5))
# Atlast this sum(last) function is returning nothing because the type of these two arguements is not same so we were returning without any value and thats why 'none' is printed here.




#Benifits = Function makes your code simpler because if u dont use function to execute this code which were seen previously then uneed to write some code again and again whenever you want to use functionality and different places.
           #Function makes your code reusable so the same code is use to add to integer values, to concatinate to string values and is also use to give the error is you provide the arguement of different types. That means you write the code once and use it multiple time.
           #When u declare functions u can test and debugg ur code in a better way.