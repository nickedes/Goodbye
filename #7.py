import sys
from math import sqrt
from itertools import count, islice
import time

def isPrime(n):
    if n < 2: return False
    for i in islice(count(3,2), int(sqrt(n)-1)//2):
        if n%i ==0:
            return False
    return True

# inputs = sys.stdin
# t = int(next(inputs))
start_time = time.time()
t = int(raw_input("enter t"))
primes = {}
primes[1] = 2
for i in range(t):
    # n = int(next(inputs))
    n = int(raw_input("enter"))
    if n==1:
        print 2
    elif n in primes:
        print primes[n] 
    else:
        i = 1
        prime = 3
        while True:
            if i >= n:
                break
            if isPrime(prime):
                primes[i+1] = prime 
                i += 1
            prime += 2
        print primes[n]
print time.time() - start_time
print primes