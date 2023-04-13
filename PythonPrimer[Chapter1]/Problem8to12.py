"""
Python allows negative integers to be used as indices into a sequence, 1.8 such as a string.
If string s has length n, and expression s[k] is used for index −n ≤ k < 0,
what is the equivalent index j ≥ 0 such that s[j] references the same element?
"""

test_array = range(20)
print(test_array)
ind = 4
print(f"Element at index = {ind} is, {test_array[ind]}")
n = len(test_array)
print(f"Element at index = {ind - n} is, {test_array[ind-n]}")

""" 
What parameters should be sent to the range constructor, 
to produce a range with values 50, 60, 70, 80?
"""
i = list(range(50,90,10))
print(i)
""" 
What parameters should be sent to the range constructor, 
to produce a 1.10 range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
"""
i = list(range(8, -9, -2))
print(i)
""" 
Demonstrate how to use Python's list comprehension syntax to 
produce the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
"""
sequence = [2**n for n in range(9)]
print(f"The required sequence is obtained by {sequence}")

""" 
Python's random module includes a function choice(data) that returns a random element 
from a non-empty sequence. The random module
includes a more basic function randrange, with parameterization similar to the built-in range function, 
that return a random choice from the given range. 
Using only the randrange function, implement your own version of the choice function.
"""

from random import randrange
def choice(data):
    n = len(data)
    rand_index = randrange(n)
    return data[rand_index]

print("Running custom choice function 5 times")

data = [i for i in range(10)]
print(f"Data array is {data}")
for i in range(5):
    print(choice(data))



