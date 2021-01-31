"""
Write a Python function fetch_middle(llists) that, given a list of lists llists, returns a new list containing the middle element from each list in llists. If the list's length is even, consider the middle element to be the average between its two central elements (i.e. for the list [1, 2, 3, 4], the middle element would be (2+3)/2 = 2.5).
Adapted from: CodingBat 

"""

def fetch_middle(llists):
    result = []
    for sub_list in llists:
        if len(sub_list) % 2 == 1:
            result.append(sub_list[len(sub_list) // 2])
        else:
            result.append(sum(sub_list[len(sub_list) // 2 - 1:len(sub_list) // 2 + 1]) / 2)
    return result