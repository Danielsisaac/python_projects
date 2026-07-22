# Strings
name = "John Doe"
age = 25
name_and_age = name
name_and_age += str(age) #This basically explains string concatenation (string addition), and it only works when both additions are strings
combination = f"His name is {name} and he is aged {age}" #The function f-strings was used here, allowing for string interpolation, which is usually done with the values being interpolated being put in curly braces
print (combination)
print(name_and_age)

# String slicing
# At the basis of string slicing, the function allows you extract a piece of a string and print it to output.
# It works using the [start:stop] and sometimes, [start:stop:step], with the step showing the rate at which letters in the string are skipped
# when using it, the number in the start section is printed, and it prints till the number in the stop section, but it doesn't print the stop index character
# However, when the stop index number is not given and is left blank, it prints from the start till the last character in the string
# in the step part, you can use the negative number (-) index to make all the characters in a string be printed in reverse

string1 = "Yo what's up?"
print (string1[::1])
print (string1[::-1])
print (string1[2:10:2])

# String manipulation methods
string2 = string1.upper()
string3 = string1.lower()
print (string2, string3)
print ((string2[:5]), string3[:5])
spaces = "     Hello, world    "
print (spaces)
stripped_spaces = spaces.strip() #The usage of the strip function removes any irrelevant trailing spaces available in the string, either before or after it
print (stripped_spaces)