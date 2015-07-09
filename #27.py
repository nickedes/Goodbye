from itertools import islice,count
from math import sqrt
import sys
def isPrime(n):
    if n < 2: return False
    for i in islice(count(3,2), int(sqrt(n)-1)//2):
        if n%i ==0:
            return False
    return True
inputs = sys.stdin
t = int(next(inputs))
nmax = 0
best_a = 0
best_b = 0
for b in xrange(3,t,2):
    if isPrime(b):
        for a in xrange(-b,b,2):
            n = 1
            while isPrime(n*n + a*n + b): n += 1
            if n>nmax: 
                nmax = n
                best_a = a
                best_b = b
print best_a,best_b