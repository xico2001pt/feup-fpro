"""
Write a Python program that, given the four components of the FPRO grade, by user input, returns the student's grade, an integer from 0 to 20, by using the formula:
grade = (LE + RE + 5 * PE + 3 * TE) / 50
The program returns:

    "Input error", if the any of the components is not between 0 and 100
    "RFC", if the PE < 40 or the TE < 40
    the grade as an integer, otherwise

"""

le = int(input())
re = int(input())
pe = int(input())
te = int(input())

if not(0 <= le <= 100 and 0 <= re <= 100 and 0 <= pe <= 100 and 0 <= te <= 100):
    print("Input error")
elif pe < 40 or te < 40:
    print("RFC")
else:
    grade = (le + re + 5 * pe + 3 * te) / 50
    print(int(grade+0.5))