"""
Write a Python function interleave(f1, f2) to combine each line from first file (f1) with the corresponding line in second file (f2), while there's lines in both files.

For example:

    Considering that exists in the current directory a file shakespeare.txt with the content of shakespeare.txt and another file with the content of monty.txt, then interleave("monty.txt", "shakespeare.txt") returns a string with the same content of mixed.txt.

"""

def interleave(f1, f2):
    result = ""
    file1, file2 = open(f1).readlines(), open(f2).readlines()
    size1, size2 = len(file1), len(file2)
    for idx in range(min(size1, size2)):
        result += file1[idx] + file2[idx]
    return result