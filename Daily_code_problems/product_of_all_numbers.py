# Problem number 2

# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Uber.
#
# Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#
# Follow-up: what if you can't use division?

list_val = [1, 2, 3, 4, 5]
list_val_2 = [3, 2, 1]

def multi_array(arr):
    multi_sum = 1
    for val in arr:
        multi_sum = multi_sum * val
    return multi_sum

def solution_1(arr):
    new_arr = []
    for idx, val in enumerate(arr):
         tmp_arr = arr[idx+1:] + arr[:idx]
         new_arr.append(multi_array(tmp_arr))

    return new_arr

print(solution_1(list_val_2))