# The split() method

# A common programming task is to break a large string down into the comprising substrings.
# The string method split() splits a string into a list of tokens. Each token is a substring that forms a part of a larger string.
# A separator is a character or sequence of characters that indicates where to split the string into tokens.

# Ex: 'Martin Luther King Jr.'.split() splits the string literal "Martin Luther King Jr." using any whitespace character as the default separator
# and returns the list of tokens ['Martin', 'Luther', 'King', 'Jr.'].

# The separator can be changed by calling split() with a string argument. Ex: 'a#b#c'.split('#') uses the "#" separator to split the string "a#b#c"
# into the three tokens ['a', 'b', 'c'].

url = input('Enter URL:\n')

tokens = url.split('/')  # Uses '/' separator
print(tokens)

# The example above shows how split() might be used to find the elements of a path to a web page; the separator used is the forward slash character '/'.
# The split() method creates a new list, ordered from left to right, containing a new string for each sequence of characters located between '/' separators.
# Thus the URL http://en.wikipedia.org/wiki/Lucille_ball is split into ['http:', '', 'en.wikipedia.org', 'wiki', 'Lucille_ball'].
# The separator character is not included in the resulting strings.

# If the split string starts or ends with the separator, or if two consecutive separators exist, then the resulting list will contain an empty string
# for each such occurrence. Ex: The consecutive forward slashes of 'http://' and the ending forward slash of '.../wiki/ethernet/' generate empty strings.
# If the separator argument is omitted from split(), thus splitting the string wherever whitespace occurs, then no empty strings are generated.

# The join() method

# The join() string method performs the inverse operation of split() by joining a list of strings together to create a single string.
# Ex: my_str = '@'.join(['billgates', 'microsoft']) assigns the string 'billgates@microsoft' to my_str. The separator '@' provides a join() method that accepts
# a single list argument. Each element in the list, from left to right, is concatenated to create a new string object with
# the separator placed between each list element. The separator can be any string, including multiple characters or an empty string.

# Use and modify this code
# web_path = [ 'www.website.com', 'profile', 'settings' ]
# separator = '/'
# url = separator.join(web_path)

# Using the split() and join() methods together

# The split() and join() methods are commonly used together to replace or remove specific sections of a string.
# Ex: A programmer may want to change 'C:/Users/Jared/report.txt' to 'C:\\Users\\Jared\\report.txt', perhaps because a different operating system
# uses different separators to specify file locations. The example below illustrates how split() and join() are used together.

# path = input('Enter file name: ')

# new_separator = input('Enter new separator: ')
# tokens = path.split('/')
# print(new_separator.join(tokens))

# Another example ...

# A programmer may also want to add, remove, or replace specific token(s) from a string.
# Ex: The program below reads in a URL and checks if the third token is 'wiki', as Wikipedia URLs follow the format of
# http://language.wikipedia.org/wiki/topic. If 'wiki' is missing from the URL, the program uses the list method insert()
# to correct the URL by adding 'wiki' before position 3.

# url = input('Enter Wikipedia URL: ')

# tokens = url.split('/')

# if 'wiki' != tokens[3]:
#     tokens.insert(3, 'wiki')
#     new_url = '/'.join(tokens)

#     print('{} is not a valid address.'.format(url))
#     print('Redirecting to {}'.format(new_url))
# else:
#     print('Loading {}'.format(url))


