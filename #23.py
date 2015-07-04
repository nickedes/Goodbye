import sys
from time import time
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

start = time()
abundant = []
for i in xrange(12,28112):
    if i < sum_divisors(i):
        abundant.append(i)

hav_abundant_sum = []
for i in xrange(1,28124):
    # if direct multiple of an abundant!
    flag = 0
    for x in abundant:
        if i%x == 0 and x != i:
            flag = 1
            hav_abundant_sum.append(i)
            break
    if flag == 0:
        # check for pair in abundant[] with sum as i
        left,right = 0,len(abundant)-1
        while left < right:
            if abundant[left] + abundant[right] == i:
                hav_abundant_sum.append(i)
                break
            elif abundant[left] + abundant[right] < i:
                left += 1
            else:
                right -= 1
# print hav_abundant_sum[:100]
total = 28123*(28124)/2
print total - sum(hav_abundant_sum)
print time()-start