# Manipulating tuples - Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)


# count() - The count() method of Tuple returns the number of times the given element appears in the tuple.
countries = ("Spain", "Italy", "India", "England", "Germany", "Spain")
print(countries.count("Spain"))


# Index() - The Index() method returns the first occurrence of the given element from the tuple. Syntax - tuple.index(element, start, end)
Tuple = (0, 1, 2, 2, 2, 3, 1, 3, 2)
res = Tuple.index(3)
print('First occurrence of 3 is', res)  # It returns index number of first Occurence. In this case return 3's index number is 5 because first occurance of 3 is index 5.
