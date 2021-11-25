import random
from typing import List, Union


def is_equal_to_k(arr, k):
    total = len(arr)
    for i in range(0, total):
        for g in range(i + 1, total):
            if arr[i] + arr[g] == k:
                return True
    return False


def is_equal_to_k_quick(arr, k):
    values: List[Union] = []

    m = int(k / 2) + 1
    for i in range(1, m):
        values.append([i, k - i])

    for val in values:
        if all(item in val for item in arr):
            return True

    return False


def generate_random_list() -> List[int]:
    return [random.randint(0, 100) for i in range(0, 50)]


if '__main__' == __name__:
    print(is_equal_to_k(generate_random_list(), random.randint(0, 100)))
    print(is_equal_to_k_quick(generate_random_list(), random.randint(0, 100)))
    print(is_equal_to_k_quick(generate_random_list(), random.randint(0, 100)))
