"""
Write a Python function academy_awards(alist) which receives a list of tuples, alist, where each tuple holds the category and the corresponding winning movie and returns a dictionary that maps each movie to the number of awards that it won.
For example:
    academy_awards([("Best Picture", "Moonlight"), ("Best Director", "La La Land"), ("Best Actor", "Manchester by the Sea"), ("Best Actress", "La La Land"), ("Best Supporting Actor", "Moonlight"),  ("Best Supporting Actress", "Fences"), ("Best Original Screenplay", "Manchester by the Sea"), ("Best Original Score", "La La Land")]) should return the dictionary: {'Moonlight': 2, 'La La Land': 3, 'Manchester by the Sea': 2, 'Fences': 1}

"""

def academy_awards(alist):
    dict1 = {}
    for tup in alist:
        dict1[tup[1]] = dict1.get(tup[1], 0) + 1
    return dict1