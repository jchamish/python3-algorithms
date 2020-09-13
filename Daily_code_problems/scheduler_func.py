# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time
from threading import Thread

def delayed_execution(f, ms):
    time.sleep(ms)
    return f()

def hello(name):
    print('Does it work {}'.format(name))

job = Thread(target=delayed_execution, args=(lambda: hello('Test'), 1.0))
job.start()
