# -*- coding: utf-8 -*-
"""
Write a Python function dogs(h_age) that receives the dog's age in human years h_age and returns the corresponding dog's age in dog's years. For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

"""

def dogs(h_age):
    return 10.5 * h_age if h_age <= 2 else 4 * (h_age - 2) + 21