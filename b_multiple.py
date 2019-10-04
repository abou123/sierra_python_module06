# Sometimes the code in a try block may generate different types of exceptions. In the previous BMI example, a ValueError was generated when the int() function
# was passed a string argument that contained letters. Other types of errors (such as NameError, TypeError, etc.) might also be generated,
# and thus a program may need to have unique exception handling code for each error type. Multiple exception handlers can be added to a try block
# by adding additional except blocks and specifying the specific type of exceptionthat each except block handles.

# An except block with no type (as in the BMI example) handles any unspecified exception type, acting as a catch-all for all other exception types.
# Good practice is to generally avoid the use of a catch-all except clause. A programmer should instead specify the particular exceptions to be handled.
# Otherwise, a program bug might be hidden when the catch-all except clause handles an unexpected type of error.

# If no exception handler exists for an error type, then an unhandled exception may occur. An unhandled exception causes the interpreter to print the exception
# that occurred and then halt.

# The following program introduces a second exception handler to the BMI program, handling a case where the user enters "0" as the height,
# which would cause a ZeroDivisionError exception to occur when calculating the BMI.

# An example

user_input = ''
while user_input != 'q':
    try:
        weight = int(input("Enter weight (in pounds): "))
        height = int(input("Enter height (in inches): "))

        bmi = (float(weight) / float(height * height)) * 703
        print('BMI:', bmi)
        print('(CDC: 18.6-24.9 normal)\n')  # Source www.cdc.gov
    except ValueError:
        print('Could not calculate health info.\n')
    except ZeroDivisionError:
        print('Invalid height entered. Must be > 0.')

    user_input = input("Enter any key ('q' to quit): ")

    # In some cases, multiple exception types should be handled by the same exception handler.
    # A tuple can be used to specify all of the exception types for which a handler's code should be executed.