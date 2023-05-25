#list is the collection the value
names = ("mark", "john", "albert", "rock")
print(names) #index of 'mark' is 0, index of 'john' is 1, index of 'albert', is 2, index of 'rock' is 3



#if i want to print only 'mark' or only ' rock'
names = ("mark", "john", "albert", "rock")
print(names[0])
print(names[3])




#if i want to print backward
names = ("mark", "john", "albert", "rock")
print(names[-1]) # it print only 'rock'



#if i want to add more vaues in names
names = ["mark", "john", "albert", "rock"]  #[] this is the sign of list, and () this is the sign of tuples
names.append("shahil")
print(names)


#if i want to add  list int the list
ages = [22,24,26,29]
names.extend(ages)
print(names)



#how to remove items from list
names = ["mark", "john", "albert", "rock", "shahil"]
ages = [22,24,26,29]
names.remove("shahil")  #remove name
ages.remove(29) #remove age
print(names)
print(ages)


# Insert element in particular index
n =[5,8,9,4,6,5,7,2]
n.sort()
n.insert(4, 99)
print(n)


# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)



#  if you want a case-insensitive sort function, use str.lower as a key function:
fruits = ["apple", "banana", "Cherry", "kiwi", "Mango"]
fruits.sort(key = str.lower)
print(fruits)



# If we want to join all the item with 'and
fruits = ["apple", "banana", "Cherry", "kiwi", "Mango"]
a = " and ".join(fruits)
print(a)

#Alternative(without join function)
fruits = ["apple", "banana", "Cherry", "kiwi", "Mango"]
for item in fruits:
  print(item,"and", end=" ")