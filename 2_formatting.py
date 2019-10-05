# Conversion specifiers

# A program commonly needs to display nicely formatted output beyond the
# ability of basic print usage (i.e., print(x)).
# Consider a program that requires the following output:

# Student ID: 00422332
# Grade percentage: 94.20%
# Notice that the student ID has two leading 0s,
# and the grade percentage uses exactly four significant digits.
# Such output is not possible using simple print statements without an
# overly complicated scheme, such as calculating
# the number of digits of the student's id number
# and manually prepending the appropriate number of 0s.

# A conversion specifier is a placeholder for some value in a string literal.
# Ex: The expression 'age is %d' % user_age uses the %d conversion specifier
# as a placeholder for the value of user_age.
# If the value of user_age was 22, the result of the expression is age is 22.
# The % character outside of the string literal
# is an operator, similar to + or /, known as the conversion operator.
# The conversion operator converts the value
# from the right side into a string and
# replaces the conversion specifier on the left with that value.
# The result of the expression is a new string with the replacements.

# Note that if only a single conversion specifier is used,
# a lone value can be supplied.
# If multiple conversion specifiers are present in the string,
# then the values should be placed in a tuple, as in
# 'age of the %s is %d' % ('cat', user_age).

# A conversion specifier includes a character (like the d in %d above),
# known as the conversion type,
# to indicate how to convert the value into the string.
# The d means integer (d stands for decimal integer),
# whereas an f stands for float.
# Ex: '%f' % 5.2 yields the string '5.200000', while '%d' % 5.2 yields
# the string '5' because the float is truncated when converted to an integer.
# Common conversion specifiers are integer (%d),
# floating-point (%f), and string (%s).

# Here are a few common conversion specifiers:

# %s == Convert to string using str()
# %d == Convert to integer
# %f == Convert to floating point
# %e == Floating point exponential format (Ex: 1.7e3)
# %% == Convert to an actual percentage sign (%)

# Text alignment and float precision

# A conversion specifier may include optional components that provide
# advanced formatting capabilities.
# One such component is a minimum field width,
# placed immediately before the conversion type, that describes
# the minimum number of characters to be inserted in the string.
# If a string value assigned to a conversion specifier is
# smaller in size than the specified minimum field width,
# then the left side of the string is padded with space characters.
# The statement print('Student name (%5s)' % 'Bob') produces the output:

# Student name (  Bob)

# The output contains an additional two spaces prior to 'Bob'
# because the minimum field width is five and Bob is only three characters
# (5 - 3 is 2).

# An additional component known as conversion flags
# alter the output of conversion specifiers.
# If the '0' conversion flag is included,
# numeric conversion types (%d, %f) add the leading 0s
# prescribed by the minimum field
# width in place of spaces.
# Other conversion flags exist, such as '-',
# which left-justifies the formatted string, adding padding
# characters to the right instead of the left.
# Multiple conversion flags may be included in the same conversion specifier.
# The conversion flags are always placed before the minimum field width:

# student_id = int(input('Enter student ID: '))
#
# print('The user entered %d' % student_id)
# print('Full 8-character student ID: %08d' % student_id)

# You might want to set how many digits to the right of a
# float-point decimal number to print.
# The optional precision component of a conversion specifier indicates
# how many digits to the right of the decimal should be included.
# The precision must follow the minimum field width
# component in a conversion specifier, and starts with a period character:
# e.g., '%.1f' % 1.725 indicates a precision of 1,
# thus the resulting string would be '1.7'.
# If the specified precision is greater
# than the number of digits available, trailing 0s are appended:
# e.g., '%.5f' % 1.5 results in the string '1.50000'. For example:

# Try this code
import math
REAL_PI = math.pi  # math library provides close approximation of pi
APPROXIMATE_PI = 22.0 / 7.0  # Approximate pi to 2 decimal places

print('pi is %f.' % REAL_PI)
print('22/7 is %f.' % APPROXIMATE_PI)
print('22/7 is accurate for 2 decimal places: %.2f' % APPROXIMATE_PI)
