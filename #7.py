import sys
from math import sqrt; from itertools import count, islice


def isPrime(n):
    if n < 2: return False
    return all(n%i for i in islice(count(2), int(sqrt(n)-1)))

inputs = sys.stdin
t = int(next(inputs))

for i in range(t):
    n = int(next(inputs))
    i = 1
    prime = 3
    while True:
        if i >= n:
            break
        if isPrime(prime):
            i += 1
        prime += 2
    print prime - 2