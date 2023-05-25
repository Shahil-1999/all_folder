#print same string in three ways either u can use single quot (' '), or u can use double quote (" "), or u can use triple quote (""" """)
a=('apple')
b=("apple")
c=("""apple""")
print(a)
print(b)
print(c)


#a='i am a single quoted string don't' ( my string start from I and end with N {T not consider})
#solution of this problem=(one back slash put just before t example) (this back slash is escape character)
a='i am single quoted string don\'t'   #escape character not shown in output
print(a)
b="i am double\" quoted string"
print(b)
c="""i am\""" triple quoted string"""
print(c)



#if i want to show back slash
a = 'i am single\quoted string don\'t'
print(a)
print(len(a))  #length of A



#join string
a='hello'
b='Shahil'
print(a+b)   # this  is called concatination operation



#if i want to print shahil 10 times
a='Shahil'
print(a*10)



#string + integer not possible
a='shahil'
b=5
print(a+b)
#if i want string + integer
a='shahil'
b=5
print(a+str(b))