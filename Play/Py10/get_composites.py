"""
Write a generator function get_composites(n) that yields a sequence of composite numbers in the interval [4, n].

There are two kinds of positive numbers: prime numbers and composite numbers. A composite number is the product of a sequence of prime numbers.

"""

def get_composites(n):
    primes = [x for x in range(2, n+1) if all(x % y != 0 for y in range(2, x))]
    composites = (x for x in range(4, n+1) if x not in primes)
    return composites