# Find the first four consecutive integers to have four distinct prime factor4.
from math import sqrt, ceil


def getPrimefactors(num):
    """
    Returns a set of prime factors of the `num`.
    """
    primes = set()
    while num % 2 == 0:
        primes.add(2)
        num /= 2
    for i in xrange(3, int(ceil(sqrt(num)+1)), 2):
        while num % i == 0:
            primes.add(i)
            num /= i
    if num > 2:
        primes.add(num)
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
        else:
            count_cons = 0
    return start - count + 1


if __name__ == '__main__':
    # 4 consecutive numbers with 4 distinct primes.
    print distinctPrimes(4, 4)
