# nowmal args
def funargs (*args):
    print(args)

lst = ["apple" , "ball", "cat", "dog"]
funargs(*lst)


# # Using for loops
# def funargs1 (*args):
#     for items in args:
#         print(items)

# lst = ["apple" , "ball", "cat", "dog"]
# funargs1(*lst)


# # **kwargs
# def funkwargs2 (**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} knows {value}")

# kw = {"shahil":"python", "rohan": "java", "manish":"c++"}
# funkwargs2(**kw)
