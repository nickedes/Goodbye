import sys
from math import sqrt
from itertools import count, islice


def isPrime(n):
    if n < 2:
        return False
    for i in islice(count(3, 2), int(sqrt(n)-1)//2):
        if n % i == 0:
            return False
    return True

inputs = sys.stdin
t = int(next(inputs))
primes = [2]
for i in range(t):
    n = int(next(inputs))
    if n == 1:
        print 2
    elif n < len(primes):
        print primes[n-1]
    else:
        if max(primes) == 2:
            start = 3
            prime = 3
        else:
            start = max(primes)
            prime = max(primes)+2
        while True:
            if n <= len(primes):
                break
            if isPrime(prime):
                primes.append(prime)
            prime += 2
        print primes[n-1]
