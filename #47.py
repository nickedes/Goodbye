# Find the first four consecutive integers to have four distinct prime factors.
from math import sqrt
from itertools import count, islice


def isPrime(n):
    """
    Checks whether the passed number is prime or not.
    """
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in islice(count(3, 2), int(sqrt(n)-1)//2):
        if n % i == 0:
            return False
    return True


def getPrimefactors(num):
    """
    Returns a set of prime factors of the `num`.
    """
    primes = set()
    for i in xrange(2, num/2):
        if isPrime(i) and num % i == 0:
            primes.add(i)
    return len(primes)


def distinctPrimes(num, count):
    """
    Parameter
    ---------
    num -- int
        The no. of distinct primes the consecutive numbers should have.
    count -- int
        The no. of consecutive numbers.
    """
    # Count of consecutive numbers found with `num` distinct primes.
    count_cons = 1
    # First number with 4 distinct primes.
    start = 2*3*5*7
    while count_cons != count:
        start += 1
        if getPrimefactors(start) == num:
            count_cons += 1
            if count_cons == 2:
                print start
        else:
            count_cons = 0
    return start - count + 1


if __name__ == '__main__':
    # 4 consecutive numbers with 4 distinct primes.
    print distinctPrimes(4, 4)
