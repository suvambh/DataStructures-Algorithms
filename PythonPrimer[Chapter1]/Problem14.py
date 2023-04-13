"""
Write a short Python function that takes a sequence of integer values
and determines if there is a distinct pair of numbers in the sequence
whose product is odd.
"""

def check_odd_product(arr):
    flag = False
    odd_dict = {}
    for i in arr:
        if i%2 != 0:
            if i not in odd_dict:
                odd_dict[i] = 1
            else:
                odd_dict[i] += 2
    if len(odd_dict) > 1:
        flag = True
    return flag

arr = [1,2,3,4]
result = check_odd_product(arr)
print(result)

"""
Write a Python function that takes a sequence of numbers and
determines if all the numbers are different from each other (that is,
they are distinct).
"""

def check_distinct(arr):
    flag = True
    hash_map = {}
    for i in arr:
        if i in hash_map:
            flag = False
            break
        else:
            hash_map[i] = 1
    return flag

arr = list(range(10))
arr[4] = 0
print(f" The array {arr} has distinct elements = {check_distinct(arr)}")

