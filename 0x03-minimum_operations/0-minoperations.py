#!/usr/bin/python3
"""
Find minimum number of copy and paste operations to create a string.

Solution: find the prime factors and return their sum.
"""
from math import sqrt


def minOperations(n):
    """Sum all the factors of n to find the 'minimum operations'.

    Args:
        n (int): number of characters

    Returns:
        int: minimum number of operations
    """
    sumFactors = 0
    if n <= 1:
        return 0
    for i in range(2, int(sqrt(n) + 1)):
        while n % i == 0:
            sumFactors += i
            n /= i
            if n <= 1:
                break
    if n > 1:
        sumFactors += int(n)
    return sumFactors
