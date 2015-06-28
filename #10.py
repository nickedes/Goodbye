# Todo: for better result, precompute sums!
import sys

def sumPrime(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]

inputs = sys.stdin
t = int(next(inputs))
primes = [2]
prime_million = sumPrime(6000000+1)
sums = {1:0}
for i in range(t):
    n = int(next(inputs))
    if n == 1:
        print 0
    elif n < 6000000:
        if n in sums:
            print sums[n]
        else:
            sum_p = 0
            for x in prime_million:
                if x <= n:
                    sum_p += x
                else:
                    break
            sums[n] = sum_p
            print sum_p
    else:
        print sum(sumPrime(n+1))