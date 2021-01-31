"""
Write a generator function batch_norm(alist, batch_size) that, given a list of integers alist, yields a normalized batch of elements of alist of a given size batch_size. Each batch must be normalized by the median value of the batch. That is, each batch is subtracted by the median within that batch. A batch is a sublist with size=batch_size.

For example:

    batch_norm([-1, 0, 1, 1, 2, 4], 3) returns a generator that produces [[-1, 0, 1], [-1, 0, 2]]
    batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5) returns a generator that produces [[9, 0, -13, 4, 0], [0.0, 4.0, 0.0, 0.0]]

"""

from statistics import median
def batch_norm(alist, batch_size):
    batches = []
    for idx in range(0, len(alist)//batch_size):
        index = idx
        batches.append(alist[idx*batch_size:idx*batch_size+batch_size])
    if len(alist)%batch_size==0:
        pass
    else:
        batches.append(alist[(index+1)*batch_size:])
    result = ([x-median(sub_batch) for x in sub_batch] for sub_batch in batches)
    return result