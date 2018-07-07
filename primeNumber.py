
# A prime number has to be a positive integer
# Divisible by exactly 2 integers(1 and itself)
# 1 is not a prime number

import random

# version 1
def isPrimeDefault(n):
    prime = True
    for i in range(2, n):
        if (n % i == 0):
            prime = False
    return prime

# version 2
def isPrime(n):
    bRet = True
    if n < 2:
        bRet = False

    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            bRet = False
            break
    return bRet

# comparing to baseline
prime_list = [False] * 102
for i in range(101):
    prime_list[i] = isPrimeDefault(i)

# examples
t = random.randint(0, 100)
print("{},{},{}".format(t, isPrime(t), prime_list[t]))
t = random.randint(0, 100)
print("{},{},{}".format(t, isPrime(t), prime_list[t]))
t = random.randint(0, 100)
print("{},{},{}".format(t, isPrime(t), prime_list[t]))
t = random.randint(0, 100)
print("{},{},{}".format(t, isPrime(t), prime_list[t]))


