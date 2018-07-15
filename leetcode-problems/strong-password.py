

import re

#A password is considered strong if below conditions are all met:

# 1) It has at least 6 characters and at most 20 characters.
# 2) It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
# 3) It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming other conditions are met).
# 4) Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to make s a strong password. If s is already strong, return 0.

# Insertion, deletion or replace of any one character are all considered as one change.

def strongPw(s):
    iRet = 0

    # contains 1 digit
    if re.search(r'\d', s, re.MULTILINE) is None:
        iRet += 1

    # upper case
    if re.search(r'[A-Z]+', s) is None:
        iRet += 1

    # lower case
    if re.search(r'[a-z]', s) is None:
        iRet += 1

    tmp = re.search(r'([a-z]{3,}|[A-Z]{3,})', s)
    if (tmp is not None):
        iRet += len(tmp.group(1)) / 3

    if (len(s)+iRet) < 6:
        iRet += 6 - (len(s)+iRet)

    if (len(s)+iRet) > 20:
        iRet = 20 - (len(s)+iRet)

    return iRet

def strongPasswordChecker(s):
    missing_type = 3
    if any('a' <= c <= 'z' for c in s): missing_type -= 1
    if any('A' <= c <= 'Z' for c in s): missing_type -= 1
    if any(c.isdigit() for c in s): missing_type -= 1

    change = 0
    one = two = 0
    p = 2
    while p < len(s):
        if s[p] == s[p - 1] == s[p - 2]:
            length = 2
            while p < len(s) and s[p] == s[p - 1]:
                length += 1
                p += 1

            change += length / 3
            if length % 3 == 0:
                one += 1
            elif length % 3 == 1:
                two += 1
        else:
            p += 1

    if len(s) < 6:
        return max(missing_type, 6 - len(s))
    elif len(s) <= 20:
        return max(missing_type, change)
    else:
        delete = len(s) - 20

        change -= min(delete, one)
        change -= min(max(delete - one, 0), two * 2) / 2
        change -= max(delete - one - 2 * two, 0) / 3
        return delete + max(missing_type, change)

print(1 == strongPw('aaa123'))
print(1 == strongPasswordChecker('aaa123'))
# print(1 == strongPw('aA123'))
# print(6 == strongPw(''))