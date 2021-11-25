# https://github.com/r1cc4rdo/daily_coding_problem
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Twitter.
#
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
#
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

from bisect import bisect_left as bisect


def coding_problem_11(str_input: str, set: str):
    tmp_arr = []
    for val in set:
        if len(str_input) > len(val):
            continue
        else:
            if str_input == val[:len(str_input)]:
                tmp_arr.append(val)

    return tmp_arr

# found online but don't work
def coding_problem_11_p2(string, set):
    dictionary = [s.lower() for s in sorted(string)]
    next_prefix = set + 'a' if set[-1] == 'z' else set[:-1] + chr(ord(set[-1]) + 1)
    return dictionary[set(dictionary, set):bisect(dictionary, next_prefix)]

words = ['able', 'abode', 'about', 'above', 'abuse', 'syzygy']
print(coding_problem_11_p2('abo', words))