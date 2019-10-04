# The format() method

# The string format() method formats text, similar to the string-formatting % operator. The format() method was initially introduced in Python 2.6
# and was meant to eventually replace the % syntax completely. However, the % syntax is so pervasive in Python programs and libraries that the language
# still supports both techniques.

# The format() method and % string-formatting syntax behave very similarly, each using value placeholders within a string literal.
# Each pair of braces {} is a placeholder known as a replacement field. A value from the format() arguments is inserted into the string depending
# on the contents of a replacement field. Three methods exist to fill in a replacement field:

# Positional: An integer that corresponds to the value's position.
#     'The {1} in the {0}'.format('hat', 'cat')
#         The cat in the hat
# Inferred positional: Empty {} assumes ordering of replacement fields is {0}, {1}, {2}, etc.
#     'The {} in the {}'.format('cat', 'hat')
#         The cat in the hat
# Named: A name matching a keyword argument.
#     'The {animal} in the {headwear}'.format(animal='cat', headwear='hat')
#         The cat in the hat

# The first two methods are based on the ordering of the values within the format() argument list.
# Placing a number inside of a replacement field automatically treats the number as the position of the desired value.
# Empty braces {} indicate that all replacement fields are positional, and values are assigned in order from left-to-right as {0}, {1}, {2}, etc.
# The positional and inferred positional methods cannot be combined. Ex: '{} + {1} is {2}'.format(2, 2, 4) is not allowed.

# The third method allows a programmer to create a keyword argument in which a name is assigned to a value from the format() keyword argument list.
# Ex: animal='cat' is a keyword argument that assigns 'cat' to {animal}. Good practice is to use the named method when formatting strings with many replacement
# fields to make the code more readable.

# A programmer can include a brace character { or } in the resulting string by using a double brace {{ or }}. Ex: '{0} {{x}}'.format('val') produces the string 'val {x}'.