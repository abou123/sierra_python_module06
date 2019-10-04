# Error-checking code is code that a programmer introduces to detect and handle errors that may occur while the program executes.
# Python has special constructs known as exception-handling constructs because they handle exceptional circumstances, another word for errors during execution.

# Consider the following program that has a user enter weight and height, and that outputs the corresponding body-mass index
# (BMI is one measure used to determine normal weight for a given height).

user_input = ''
while user_input != 'q':
    weight = int(input("Enter weight (in pounds): "))
    height = int(input("Enter height (in inches): "))

    bmi = (float(weight) / float(height * height)) * 703
    print('BMI:', bmi)
    print('(CDC: 18.6-24.9 normal)\n')
    # Source www.cdc.gov

    user_input = input("Enter any key ('q' to quit): ")