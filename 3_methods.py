# String objects have many useful methods to do things like replacing characters, converting to lowercase, capitalizing the first character, etc.
# The methods are made possible due to a string's implementation as a class, which for purposes here can just be thought of as a mechanism supporting
# a set of methods for a particular type of object.

# Finding and replacing

# A common task for a programmer is to edit the contents of a string. Recall that string objects are immutable -- once created, strings can not be changed.
# To update a string variable, a new string object must be created and bound to the variable name, replacing the old object.
# The replace string method provides a simple way to create a new string by replacing all occurrences of a substring with a new substring.

#     replace(old, new) -- Returns a copy of the string with all occurrences of the substring old replaced by the string new.
#         The old and new arguments may be string variables or string literals.
#     replace(old, new, count) -- Same as above, except only replaces the first count occurrences of old.

# phrase = 'One day I will have three goats, six horses, and nine llamas.'
	
# # Replace English with Spanish.
# phrase = phrase.replace('one', 'uno')
# phrase  = phrase.replace('two', 'dos')
# phrase = phrase.replace('three', 'tres')
# phrase = phrase.replace('four', 'cuatro')
# phrase = phrase.replace('five', 'cinco')
# phrase = phrase.replace('six', 'seis')
# phrase  = phrase.replace('seven', 'siete')
# phrase  = phrase.replace('eight', 'ocho')
# phrase = phrase.replace('nine', 'nueve')
	
# print('Translation:', phrase)

# Some methods are useful for finding the position of where a character or substring is located in a string:

# find(x) -- Returns the position of the first occurrence of item x in the string, else returns -1. x may be a string variable or string literal. Recall that in a string the first position is number 0, not 1. If my_str is 'Boo Hoo!':
#     my_str.find('!')  # Returns 7
#     my_str.find('Boo')  # Returns 0
#     my_str.find('oo')  # Returns 1 (first occurrence only)
# find(x, start) -- Same as find(x), but begins the search at position start:
#     my_str.find('oo', 2)  # Returns 5
# find(x, start, end) -- Same as find(x, start), but stops the search at position end:
#     my_str.find('oo', 2, 4)  # Returns -1 (not found)
# rfind(x) -- Same as find(x) but searches the string in reverse, returning the last occurrence in the string.

# Another useful function is count, which counts the number of times a substring occurs in the string:

# count(x) -- Returns the number of times x occurs in the string.
#     my_str.count('oo')  # Returns 2

# Note that methods such as find() and rfind() are useful only for cases where a programmer needs to know the exact location of the character or substring in the string.
# If the exact position is not important, than the in membership operator should be used to check if a character or substring is contained in the string:

# An involved example of string methods and formatting in action == Hangman

# word = 'onomatopoeia'
# num_guesses = 10

# hidden_word = '-' * len(word)

# guess = 1

# while guess <= num_guesses and '-' in hidden_word:
#     print(hidden_word)
#     user_input = input('Enter a character (guess #%d): ' % guess)
    
#     if len(user_input) == 1:
#         # Count the number of times the character occurs in the word
#         num_occurrences = word.count(user_input)
    
#         # Replace the appropriate position(s) in hidden_word with the actual character.
#         position = -1
#         for occurrence in range(num_occurrences):
#             position = word.find(user_input, position+1)  # Find the position of the next occurrence
#             hidden_word = hidden_word[:position] + user_input + hidden_word[position+1:]  # Rebuild the hidden word string
    
#         guess += 1
        
# if not '-' in hidden_word:
#     print('Winner!', end=' ')        
# else:
#     print('Loser!', end=' ')

# print('The word was %s.' % word)

# Comparing strings

# String objects may be compared using relational operators (<, <=, >, >=), equality operators (==, !=), membership operators (in, not in), and identity operators
# (is, is not).

# Evaluation of relational and equality operator comparisons occurs by first comparing the corresponding characters at element 0, then at element 1, etc.,
# stopping as soon as a determination can be made. For an equality (==) comparison, the two strings must have the same length and every corresponding character 
# pair must be the same. For a relational comparison (<, >, etc.), the result will be the result of comparing the ASCII/Unicode values of the first differing character
# pair.

# A few examples ...
# Test                            result  Why?
# 'Hello' == 'Hello'	            True	The strings are exactly identical values
# 'Hello' == 'Hello!'	            False	The left hand string does not end with '!'
# 'Yankee Sierra' > 'Amy Wise'	True	The first character of the left side 'Y' is "greater than" (in ASCII value) the first character of the right side 'A'
# 'Yankee Sierra' > 'Yankee Zulu'	False	The characters of both sides match until the second word. The first character of the second word on the left 'S' is not "greater than" (in ASCII value) the first character on the right side 'Z'
# 'seph' in 'Joseph'	            True	The substring 'seph' can be found starting at the 3rd position of 'Joseph'
# 'jo' in 'Joseph'	            False	'jo' (with a lowercase 'j') is not in 'Joseph' (with an uppercase 'J')

# Two string variables can be compared character by character using their ASCII values.
# Recall that ASCII values are an integer value representation of a character. 'A' is represented by the integer value 65, 'B' by 66, 'C' by 67, and so on.
# An ASCII table provides a quick lookup of ASCII values. There are many ASCII tables available online, for example www.asciitable.com.

# Can you write a test that compares two words?  Can you predict the result?

# We can also test for equality and inequality using 'is' and 'is not' operators.  It is a best practice to stick with ==.

# student_name = input('Enter student name:\n')

# if student_name is 'Amy Adams':
#     print('Identity operator: True')
# else:
#     print('Identity operator: False')

# if student_name == 'Amy Adams':
#     print('Equality operator: True')
# else:
#     print('Equality operator: False')

# Because comparison uses the encoded values of characters (ASCII/Unicode), comparison may not behave intuitively for some situations.
# Comparisons are case-sensitive, so 'Apple' does not equal 'apple'. In particular, because the encoded value for 'A' is 65, and for 'a' is 97,
# then 'Apple' is less-than 'apple'. Furthermore, 'Banana' is less than 'apple', because 'B' is 66 while 'a' is 97.

# A number of methods are available to help manage string comparisons. The list below describes the most commonly used methods;
# a full list is available at docs.python.org.

# Methods to check a string value that returns a True or False Boolean value:

# isalnum() -- Returns True if all characters in the string are lowercase or uppercase letters, or the numbers 0-9.
# isdigit() -- Returns True if all characters are the numbers 0-9.
# islower() -- Returns True if all characters are lowercase letters.
# isupper() -- Return True if all cased characters are uppercase letters.
# isspace() -- Return True if all characters are whitespace.
# startswith(x) -- Return True if the string starts with x.
# endswith(x) -- Return True if the string ends with x.

# A programmer often needs to transform two strings into similar formats to perform a comparison.
# The list below shows some of the more common string methods that create string copies, altering the case or amount of whitespace of the original string:

# Methods to create new strings:

# capitalize() -- Returns a copy of the string with the first character capitalized and the rest lowercased.
# lower() -- Returns a copy of the string with all characters lowercased.
# upper() -- Returns a copy of the string with all characters uppercased.
# strip() -- Returns a copy of the string with leading and trailing whitespace removed.
# title() -- Returns a copy of the string as a title, with first letters of words capitalized.

# A user may enter any one of the non-equivalent values 'Bob' , 'BOB ', or 'bob' into a program that reads in names.
# The statement name = input().strip().lower() reads in the user input, strips all whitespace, and changes all the characters to lowercase.
# Thus, user input of 'Bob', 'BOB ', or 'bob' would each result in name having just the value 'bob'.

# Good practice when reading user-entered strings is to apply transformations when reading in data (such as input),
# as opposed to later in the program. Applying transformations immediately limits the likelihood of introducing bugs because the user entered an unexpected string value.
# Of course, there are many examples of programs in which capitalization or whitespace should indicate a unique string -- the programmer should use discretion
# depending on the program being implemented.

# Another big example ...

# The example program below shows how the above methods might be used to store passenger names and travel destinations in a database.
# The use of strip(), lower(), and upper() standardize user-input for easy comparison.

# Run the program below and add some passengers into the database. Add a duplicate passenger name, using different capitalization, and print the list again.

# menu_prompt = ('Available commands:\n'
#                '  (add) Add passenger\n'
#                '  (del) Delete passenger\n'
#                '  (print) Print passenger list\n'
#                '  (exit) Exit the program\n'
#                'Enter command:\n')

# destinations = ['PHX', 'AUS', 'LAS'] 

# destination_prompt = ('Available destinations:\n'
#                       '(PHX) Phoenix\n'
#                       '(AUS) Austin\n'
#                       '(LAS) Las Vegas\n'
#                       'Enter destination:\n')

# passengers = {}

# print('Welcome to Mohawk Airlines!\n')
# user_input = input(menu_prompt).strip().lower()

# while user_input != 'exit':
#     if user_input == 'add':
#         name = input('Enter passenger name:\n').strip().upper()
#         destination = input(destination_prompt).strip().upper()
#         if destination not in destinations:
#             print('Unknown destination.\n')
#         else:
#             passengers[name] = destination
            
#     elif user_input == 'del':
#         name = input('Enter passenger name:\n').strip().upper()
#         if name in passengers:
#             del passengers[name]

#     elif user_input == 'print':
#         for passenger in passengers:
#             print('%s --> %s' % (passenger.title(), passengers[passenger]))
#     else:
#         print('Unrecognized command.')

#     user_input = input('Enter command:\n').strip().lower()

