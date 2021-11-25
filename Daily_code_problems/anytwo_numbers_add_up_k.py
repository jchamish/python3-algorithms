# Problem Number 1

# Good morning! Here's your coding interview problem for today.
#
# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?

import random

array_numbers = [10, 15, 3, 7]

# N^2
def sulotion_1(arr, k):
    for idx, val in enumerate(arr):
        for val_2 in arr[idx:]:
            if val+val_2 == k:
                return True
    return False

def sulotion_2(arr, k):
    for idx, val in enumerate(arr):
        remainder = k - val
        if remainder in arr[idx:]:
            return True
    return False

random_number = random.randint(1,21)

print(random_number)
print(sulotion_1(array_numbers, random_number))
print(sulotion_2(array_numbers, random_number))