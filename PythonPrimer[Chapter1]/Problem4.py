""" Write a short Python function that takes a positive integer n and returns the sum of the
squares of all the positive integers smaller than n ”
"""
import math

def sum_till_sqrt_of(n):
    """ Algorithm to add sum till square root of input number"""
    sqrt_n = int(math.sqrt(n))
    test = [t for t in range(sqrt_n)]
    sum_till_sqrt = 0
    for i in test:
        sum_till_sqrt += i
    print(sum_till_sqrt)


n = int(input("Enter number "))
sum_till_sqrt_of(n)
