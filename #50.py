from itertools import count, islice
from math import sqrt


def isPrime(n):
    """
    Checks whether n is prime or not.
    """
    if n < 2 or n % 2 == 0:
        return False
    for i in islice(count(3, 2), int(sqrt(n)-1)//2):
        if n % i == 0:
            return False
    return True


def getPrimes(num):
    """
    Generate a list of prime numbers upto num.
    """
    primes = [2]
    for n in xrange(3, num, 2):
        if isPrime(n):
            primes.append(n)
    return primes


def sum_primes():
    """
    """
    limit = 1000000
    gt = []
    list_primes = getPrimes(limit)
    print(sum(list_primes[:23]))
    cons_prime = 2
    num = 3
    while True:
        if cons_prime > limit:
            break
        if num in list_primes and num+cons_prime in list_primes:
            gt.append(num+cons_prime)
            cons_prime += num
        elif isPrime(num):
            cons_prime += num
        num += 2
        # if len(gt) > 10:
        #     print gt[-1]
    return (gt,num)


if __name__ == '__main__':
    print sum_primes()
