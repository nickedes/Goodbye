import sys
from math import sqrt
from itertools import count, islice


def isPrime(n):
    if n < 2: return False
    for i in islice(count(3,2), int(sqrt(n)-1)//2):
        if n%i ==0:
            return False
    return True

inputs = sys.stdin
t = int(next(inputs))
primes = [2]
for i in range(t):
    n = int(next(inputs))
    prime,sum_p = 3,0
    if n == 1:
        print 0
    elif n == 2:
        print 2
    elif n <= max(primes):
        for x in primes:
            if x <= n: sum_p += x
        print sum_p
    else:
        if max(primes) > 2:
            prime = max(primes)+2
        while max(primes) < n:
            if isPrime(prime):
                primes.append(prime)
            prime += 2
        for x in primes:
            if x <= n: sum_p += x
        print sum_p