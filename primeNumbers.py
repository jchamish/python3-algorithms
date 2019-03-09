
import random
# prime numbers
# A prime number has to be a positive integer
# Divisible by exactly 2 integers (1 and itself)
# 1 is not a prime number

def isPrime(n):
    bRet = True
    if n < 2:
        bRet = False

    for i in range(2, n):
            if n % i == 0:
                bRet = False
    return bRet


def isPrimeFast(n):
    if n < 2:
        return False

    for i in range(2, int(n ** 0.5)+1, 2):
        if n % i == 0:
            return False
            break
    return True


print("{},{}".format(1, isPrime(1)))
t = random.randint(0, 100)
print("{},{}".format(t, isPrime(t)))
print("{},{}".format(t, isPrimeFast(t)))
t = random.randint(0, 100)
print("{},{}".format(t, isPrime(t)))
print("{},{}".format(t, isPrimeFast(t)))
