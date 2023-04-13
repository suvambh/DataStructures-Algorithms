"""
Write a pseudo-code description of a function that reverses a list of n
integers, so that the numbers are listed in the opposite order than they
were before, and compare this method to an equivalent Python function for doing the same thing.
"""

from timeit import default_timer as timer

def rev_number(arr):
    n = len(arr)//2
    for i in range(n):
        arr[i], arr[-(1+i)] = arr[-(1+i)], arr[i]

arr = list(range(1000))

start = timer()
rev_number(arr)
end = timer()
print(arr)
print(f"Time taken to execute code = {(end - start)*10**6} milli seconds ")

start2 = timer()
arr2 = reversed(arr)
end2 = timer()
print(arr2)
print(f"Time taken to execute code using inbuilt reversed = {(end2 - start2)*10**6} milli seconds ")


