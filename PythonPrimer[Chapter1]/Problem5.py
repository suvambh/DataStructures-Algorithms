""" Give a single command that computes the sum from Exercise R-1.4,
relying on Python's comprehension syntax and the built-in sum function.”
"""

import math
n = int(input("Enter number "))
sum_till_sqrt = sum([i for i in range(int(math.sqrt(n)))])
print(sum_till_sqrt)

