def count(lst):
    even = 0
    odd = 0
    
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


lst = [2,5,9,74,45,63,78,99,41,230,123]
even, odd = count(lst)
print("Even number is: {} and odd number is {}".format(even, odd))

