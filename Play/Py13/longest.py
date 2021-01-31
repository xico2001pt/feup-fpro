"""
Write a Python function longest(filename) that given the string filename returns the longest word in the text file. Do not worry about the punctuation.

For example:

    Considering that exists in the current directory a file shakespeare.txt with the content of shakespeare.txt, then longest("shakespeare.txt") returns the string "self-substantial"
    Considering that exists in the current directory a file monty.txt with the content of monty.txt, then longest("monty.txt") returns the string "tree-sloths"

Adapted from: www.w3resource.com/python-exercises 

"""

def longest(filename):
    result, biggest = "", 0
    with open(filename) as f:
        for line in f.readlines():
            for word in line.strip().split():
                if len(word) > biggest:
                    biggest = len(word)
                    result = word
    return result