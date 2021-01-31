# -*- coding: utf-8 -*-
"""
Write a Python function change(money) that converts a given amount of money (≥ 0) into several Euro coins. Minimize the number of coins given.

The return value should be a dictionary specifying how many coins of each type should be given to the customer. The keys of the dictionary should correspond to each coin: from 0.01 (1 cent) all the way up to 2.00 (2 euros).

Using if-else is forbidden.

"""

def change(money):
    result = {2.0: 0, 1.0: 0, 0.5: 0, 0.2: 0, 0.1: 0, 0.05: 0, 0.02: 0, 0.01: 0}
    money *= 100
    for coin in list(result.keys()):
        result[coin] = int(money / (100 * coin))
        money %= 100 * coin
    return result