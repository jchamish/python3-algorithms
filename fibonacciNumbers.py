import random
import datetime

from typing import List


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_dynamic(n) -> int:
    if 0 < n <= 2:
        return 1

    if n > 2:
        cal_list: List[int] = [0] * (n + 1)
        cal_list[0] = 0
        cal_list[1] = 1

        for i in range(2, n + 1):
            cal_list[i] = cal_list[i - 1] + cal_list[i - 2]

        return cal_list[n]

    return 0


if __name__ == '__main__':
    random.seed(datetime.datetime.now())
    for i in range(5):
        t = random.randint(0, 15)
        print(f"fib_r:{t},{fib(t)}")
        print(f"fib_d:{t},{fib_dynamic(t)}")
        print("-" * 10)
