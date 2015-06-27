import sys
import time
from math import sqrt
from itertools import count, islice


def isPrime(n):
    if n < 2: return False
    for i in islice(count(3,2), int(sqrt(n)-1)//2):
        if n%i ==0:
            return False
    return True

# inputs = sys.stdin
# t = int(next(inputs))
start_time = time.time()
t = 1
primes = [2]
for i in range(t):
    # n = int(next(inputs))
    n = 1000
    num = {}
    for i in islice(count(2), n-1):
        num[i] = 0
    print time.time() - start_time
    p = 2
    while True:
        flag = 0
        for data in num:
            if num[data] == 0 and data % p == 0 and data > p:
                num[data] = 1
        for key,value in num.items():
            if key > p and value == 0:
                flag = 1
                p = key
                break
        if flag == 0:
            break
        print time.time() - start_time
    sum_p = 0
    for key,value in num.items():
        if value == 0:
            sum_p += key
    print sum_p
    print time.time() - start_time