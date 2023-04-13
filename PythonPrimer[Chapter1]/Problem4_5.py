""" Write a short Python function that takes a positive integer n and returns the sum of the
squares of all the positive integers smaller than n
"""
import math

def sum_till(n):
    """ Algorithm to add sum till square root of input number"""
    test = [t**2 for t in range(n)]
    sum_till_sqrt = 0
    for i in test:
        sum_till_sqrt += i
    return(sum_till_sqrt)

n = int(input("Enter number "))
print(f"Not using sum function the sum is {sum_till(n)}")

""" Give a single command that computes the sum from Exercise R-1.4,
relying on Python's comprehension syntax and the built-in sum function.
"""

sum_till_sqrt = sum([i**2 for i in range(n)])
print(f"Using sum function, sum is {sum_till_sqrt}")
