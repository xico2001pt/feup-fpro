"""
Write a boolean function in Python called validate that validates a grade by outputting whether the grade is correct or incorrect. A grade is a number between 0 and 100.

You cannot use if.

"""

def validate(grade):
    return ((type(grade) == float or type(grade) == int) and (grade >= 0 and grade <= 100))