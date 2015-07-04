import sys
from math import sqrt
def sum_divisors(num):
    """
    Gives a dict of prime factors of the number num, along with their powers.

    Then calculates the sum of all possible divisors from the prime factors.
    """
    n = num
    prime_fac = {}
    if num%2 == 0:
        prime_fac[2] = 0
    while num%2 == 0:
        prime_fac[2] += 1
        num /= 2
    for i in range(3,int(sqrt(num))+1,2):
        if num%i == 0:
            prime_fac[i] = 0
        while num%i == 0:
            prime_fac[i] += 1
            num /= i
    if num > 2:
        prime_fac[num] = 1
    sum_factors = 1
    for prime in prime_fac:
        sum_factors *= (pow(prime, prime_fac[prime]+1)-1)/(prime -1)
    return sum_factors-n

inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    n = int(next(inputs))
    am = []
    for i in xrange(2,n+1):
        num = sum_divisors(i)
        if i == sum_divisors(num) and num != i and i not in am and num <= n:
            am.append(i)
            am.append(num)
    print sum(am)