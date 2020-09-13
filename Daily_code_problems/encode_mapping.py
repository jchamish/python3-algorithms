
# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
#
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
#
# You can assume that the messages are decodable. For example, '001' is not allowed.

import string

t = list(string.ascii_lowercase)

def count_ways(encoded_msg,mapping):
    if len(encoded_msg) == 1:
        return 1 if encoded_msg in mapping else 0
    elif len(encoded_msg)==2:
        if(encoded_msg.startswith('0')):
            return 0
        if encoded_msg in mapping:
            return 2
        if not encoded_msg.endswith('0'):
            return 1
        return 0
    else:
        x = 1 if encoded_msg[:1] in mapping else 0
        y = 1 if encoded_msg[:2] in mapping else 0
        return x*count_ways(encoded_msg[1:], mapping) + y*count_ways(encoded_msg[2:], mapping)

if __name__ == "__main__":
    mapping = set()
    for i in range(0,26):
       mapping.add(str(i+1))

    print(count_ways('111',mapping))
    print(count_ways('001',mapping))

def coding_problem_7(s):
    """
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
    Examples:
    >>> coding_problem_7('111')  # possible interpretations: 'aaa', 'ka', 'ak'
    3
    >>> coding_problem_7('2626')  # 'zz', 'zbf', 'bfz', 'bfbf'
    4
    """
    symbols = map(str, range(1, 27))
    if not s:
        return 1

    matches = filter(lambda symbol: s.startswith(symbol), symbols)
    encodings = [coding_problem_7(s[len(m):]) for m in matches]
    return sum(encodings)

