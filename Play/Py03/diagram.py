# -*- coding: utf-8 -*-
"""
Rewrite the following flow diagram as a Python script.
<diagram.png>

Note that := is assignment.

"""

L = int(input())
S = int(input())
R = L

def fun_if(S, R):
    if S > R:
        pass
    else:
        while not(S > R):
            R = R - S
    return R

if R > S:
    pass
else:
    L = R
    R = S
    S = L

R = fun_if(S, R)

if R == 0:
    pass
else:
    while R != 0:
        L = R
        R = S
        S = L
        R = fun_if(S, R)
print(S)