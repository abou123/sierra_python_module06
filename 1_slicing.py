# Slicing Basics

# Strings are a sequence type, having characters ordered by index from left to right.
# An individual character is read using brackets. Ex: str[5] reads the character at index 5 of the string str.

# In future programs, you may need to read more than one character at a time. Multiple consecutive characters can be read using slice notation.
# Slice notation has the form my_str[start:end], which creates a new string whose value mirrors the characters of my_str from indices start to end - 1.
# If my_str is 'Sierra', then my_str[0:3] yields string 'Sie'. Other sequence types like lists and tuples also support slice notation.

url = 'http://en.wikipedia.org/wiki/Turing'
domain = url[7:23]  # Read 'en.wikipedia.org' from url
print(domain)

# The last character of the slice is one location before the specified end. Consider the string my_str = 'John Doe'.
# The slice my_str[0:4] includes the element at index 0 (J), 1 (o), 2 (h), and 3 (n), but not 4, thus yielding 'John'.
# The space character at index 4 is not included. Similarly, my_str[4:7] would yield ' Do', including the space character this time.
# To retrieve the last character, an end index greater than the length of the string can be used. Ex: my_str[5:8] or my_str[5:10] both yield the string 'Doe'.

# Negative numbers can also be used to specify an index relative to the end of the string. Ex: If the variable my_str is 'Jane Doe!?',
# then my_str[0:-2] yields 'Jane Doe' because the -2 refers to the second-to-last character '!' (and the character at the end index is not included in the result string).

# Predict the output:

#my_str = 'The cat in the hat'
#print(my_str[0:3])

# Your guess:

# Predict the output:

# my_str = 'The cat in the hat'
# print(my_str[3:7])

# Your guess:

# Slicing and slicing operations

# The Python interpreter creates a new string object for the slice. Thus, creating a slice of the string variable my_str,
# and then changing the value of my_str, does not also change the value of the slice.

# Try this code
# my_str = "The cat jumped the brown cow"
# animal = my_str[4:7]
# print('The animal is a %s' % animal)

# my_str = 'The fox jumped the brown llama'
# print('The animal is still a', animal)  # animal variable remains unchanged.

#A programmer often wants to read all characters that occur before or after some index in the string.
# Omitting a start index, such as in my_str[:end] yields the characters from indices 0 to end-1.
# Ex: my_str[:5] reads indices 0-4. Similarly, omitting the end index yields the characters from the start index to the end of the string.
# Ex: my_str[5:] yields all characters at and after index 5.

# Variables can also be used in place of literals to specify slice notation start and end indices. Ex: my_str[x:y].

# Try this code
# usr_text = input('Enter a string: ')
# print()

# first_half = usr_text[:len(usr_text)//2]
# last_half = usr_text[len(usr_text)//2:]

# print('The first half of the string is "%s"' % first_half)
# print('The second half of the string is "%s"' % last_half)

# The slice stride

# Slice notation also provides for a third argument, known as the stride. The stride determines how much to increment the index after reading each element.
# For example, my_str[0:10:2] reads every other element between 0 and 10. The stride defaults to 1 if not specified.

#Try this code
# numbers = '0123456789'

# print('All numbers: %s' % numbers[::])
# print('Every other number: %s' % numbers[::2])
# print('Every third number between 1 and 8: %s' % numbers[1:9:3])

