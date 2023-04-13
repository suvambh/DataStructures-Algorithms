"""
Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the odd positive integers smaller than n.
"""

import math
def sum_of_odd_till(n):

    sum_of_odd = 0
    for i in range(n):
        if i%2 == 0:
            continue
        else:
            sum_of_odd += i
    return sum_of_odd

n = int(input("Enter number "))

print(f"Sum of odd numbers less than {n} is {sum_of_odd_till(n)} ")

print(f"Sum of odd numbers less than {n} using sum() and list comprehension"
      f" is {sum([i for i in range(1, n, 2)])}")



