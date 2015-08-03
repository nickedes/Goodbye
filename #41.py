from math import sqrt
from itertools import count, islice


def check_pandigital(string, s=9):
    string = str(string)
    return len(string) == s and not '1234567890'[:s].strip(string)


def isPrime(n):
    if n < 2 or n % 2 == 0:
        return False
    for i in islice(count(3, 2), int(sqrt(n)-1)//2):
        if n % i == 0:
            return False
    return True


def PrimePandigital():
    """The pandigital for n=9,8,6,5 is always a multiple of 3.
    Returns
    -------
    Maximum pandigital prime.
    """
    for x in xrange(7654321, 7123456+1, -2):
        if isPrime(x) and check_pandigital(x, 7):
            return x

print PrimePandigital()
