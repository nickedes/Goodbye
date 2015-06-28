import sys
from math import sqrt
from itertools import count, islice

def sumPrime(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

inputs = sys.stdin
t = int(next(inputs))
primes = [2]
prime_million = sumPrime(2000000+1)
for i in range(t):
    n = int(next(inputs))
    if n == 1:
        print 1
    elif n < 2000000:
        sum_p = 0
        for x in prime_million:
            if x <= n:
                sum_p += x
            else:
                break
        print sum_p
    else:
        print sum(sumPrime(n+1))