"""
Write a Python function repeated_letter(s) which returns the first character to repeat itself.
Adapted from: Code Wars

"""

def repeated_letter(s):
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return s[i]