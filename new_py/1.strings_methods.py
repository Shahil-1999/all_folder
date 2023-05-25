# Strings are immutable
a = "!!!Harry!! !!!!!!!!! Harry"
print(len(a))
print(a)
print(a.upper())    #The upper() method converts a string to upper case.

print(a.lower())    #The lower() method converts a string to lower case.

print(a.rstrip("!"))    #the rstrip() removes any trailing characters not leadong characters.

str2 = " Silver Spoon "
print(str2.strip())         #The strip() method removes any white spaces before and after the string.



print(a.replace("Harry", "John"))   #The replace() method replaces all occurences of a string with another string.

print(a.split(" ")) #The split() method splits the given string at the specified instance and returns the separated strings as list items.



blogHeading = "introduction tO jS"
print(blogHeading.capitalize()) #The capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.



str1 = "Welcome to the Console!!!"
print(str1.center(50)) #The center() method aligns the string to the center as per the parameters given by the user.

str1 = "Welcome to the Console!!!"
print(str1.center(50, ".")) #We can also provide padding character. It will fill the rest of the fill characters provided by the user.





str2 = "Abracadabra"
countStr = str2.count("a")  #The count() method returns the number of times the given value has occurred within the given string.
print(countStr)

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!")) #The endswith() method checks if the string ends with a given value. If yes then return True, else return False.


str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))   #We can even also check for a value in-between the string by providing start and end index positions.



str1 = "He's name is Dan. He is an honest man."
print(str1.find("ishh"))    #The find() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.

print(str1.index("name"))     #The index() method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.



str1 = "WelcomeToTheConsole"
print(str1.isalnum())   #The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.



str1 = "Welcome"
print(str1.isalpha())   #The isalnum() method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.

str1 = "hello world"
print(str1.islower())   #The islower() method returns True if all the characters in the string are lower case, else it returns False.



str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())   #The isprintable() method returns True if all the values within the given string are printable, if not, then return False.



#The isspace() method returns True only and only if the string contains white spaces, else returns False.
str1 = "         "       #using Spacebar
print(str1.isspace())
str2 = "  "       #using Tab
print(str2.isspace())


str1 = "World Health Organization" 
print(str1.istitle())   #The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper())   #The isupper() method returns True if all the characters in the string are upper case, else it returns False.



str1 = "Python is a Interpreted Language" 
print(str1.startswith("Python"))    #The staerswith() method checks if the string starts with a given value. If yes then return True, else return False.



str1 = "python is a Interpreted Language" 
print(str1.swapcase())  #The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.



str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) #The title() method capitalizes each letter of the word within the string.


