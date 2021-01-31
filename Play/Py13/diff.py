"""
In Linux, there is a command called diff which displays the difference between two files. Write a function diff(filename1, filename2) that receives two filenames filename1 and filename2 as its parameters and returns the contiguous difference between the files until two lines finally match again.

For example, given the two files:

1. file1d.txt

I need to buy apples.
I need to run the laundry.
I need to wash the dog.
I need to get the car detailed.
And then I go sleep!

2. file2d.txt

I need to buy apples.
I need to do the laundry.
I need to wash the car.
And then I go sleep!

    diff("file1d.txt", "file2d.txt") should return the string

- I need to run the laundry.
- I need to wash the dog.
- I need to get the car detailed.
+ I need to do the laundry.
+ I need to wash the car.

"""

def diff(filename1, filename2):
    with open(filename1, "r") as file:
        f1 = file.readlines()
    with open(filename2, "r") as file:
        f2 = file.readlines()
    
    min_size, max_size = min([len(f1), len(f2)]), max([len(f1), len(f2)])
    intervals = [i for i in range(min_size) if f2[i] == f1[i]] + [max_size]
    res, min_val = "", 0
    for val in intervals:
        for i in range(min_val, val):
            if i < len(f1):
                line = f1[i]
                if line not in f2:
                    res += "- " + line        
        for i in range(min_val, val):
            if i < len(f2):
                line = f2[i]
                if line not in f1:
                    res += "+ " + line
        min_val = val
    return res