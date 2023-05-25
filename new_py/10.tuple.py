# tuples - Tuples are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed within round brackets (). Tuples are unchangeable meaning we can not alter them after creation.

tuple1 = (1,2,2,3,5,4,6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)



# Tuples Indexes - Each item/element in a tuple has its own unique index. This index can be used to access any particular item from the tuple. The first item has index [0], second item has index [1], third item has index [2] and so on

country = ("Spain", "Italy", "India",)
#            [0]      [1]      [2]


# positive Indexing - As we have seen that tuple items have index, as such we can access items using these indexes.

country = ("Spain", "Italy", "India",)

print(country[0])



# Negative Indexing - Similar to positive indexing, negative indexing is also used to access items, but from the end of the tuple. The last item has index [-1], second last item has index [-2], third last item has index [-3] and so on.

country = ("Spain", "Italy", "India",)

print(country[-2])


# Check for Items - We can check if a given item is present in the tuple. This is done using the in keyword.
country = ("Spain", "Italy", "India", "Germany","Canada")
if "Italy" in country:
    print("Yes")



# Range of Index - You can print a range of tuple items by specifying where do you want to start, where do you want to end and if you want to skip elements in between the range. Syntax = Tuple[start : end : jumpIndex]
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])     #using positive indexes
print(animals[-7:-2])   #using negative indexes