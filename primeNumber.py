# A prime number has to be a positive integer
# Divisible by exactly 2 integers(1 and itself)
# 1 is not a prime number

import random


def is_prime_default(n):
    prime = True
    for i in range(2, n):
        if n % i == 0:
            prime = False
    return prime


def is_prime(n):
    b_ret = True
    if n < 2:
        b_ret = False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            b_ret = False
            break
    return b_ret


def is_prime_fast(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5)+1, 2):
        if n % i == 0:
            return False
    return True


prime_list = [False] * 102
for i in range(101):
    prime_list[i] = is_prime_default(i)


if __name__ == '__main__':
    t = random.randint(0, 100)
    print("{},{},{}".format(t, is_prime(t), prime_list[t]))
    t = random.randint(0, 100)
    print("{},{},{}".format(t, is_prime(t), prime_list[t]))
    t = random.randint(0, 100)
    print("{},{},{}".format(t, is_prime(t), prime_list[t]))
    t = random.randint(0, 100)
    print("{},{},{}".format(t, is_prime(t), prime_list[t]))

    print("{},{}".format(1, is_prime(1)))
    t = random.randint(0, 100)
    print("{},{}".format(t, is_prime(t)))
    print("{},{}".format(t, is_prime_fast(t)))
    t = random.randint(0, 100)
    print("{},{}".format(t, is_prime(t)))
    print("{},{}".format(t, is_prime_fast(t)))