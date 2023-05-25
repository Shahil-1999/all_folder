a = {'name': 'max', 'age': 20, }
print(a)
# dictionary is a list of key values pairs. All these values which is you see here before colon are called keys. And whatever you see after colon is called values.
# you can access the values from a dictionary based upon their keys.
print(a['name'])

# what type of datatype you can store in a dictionary
b = {'name':'tom', 15:15, 12.1:12.1, (2,3):5}
print(b)   # you can insert string, number, float values, tuples

#you can also add new key
a['surname']='cruise'
print(a)

# you can also remove any key
a.pop('surname')
print(a)

# you can also clear the values
b.clear()
print(b)

# you can also delete the dictionary
# del b
# print(b)

#you can also update the value in dictionary
a['name'] = 'manish'
print(a)
# alternate
a.update({'name': 'manish'})
print(a)

# list out all the keys
print(a.keys())

# list out all the values
print(a.values())

# you can also see key and values pair
a.items()
print(a)


# list out the content of a dictionary
a.popitem()
print(a)     # it removes the last key values pair which you have added or updated