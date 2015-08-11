from math import sqrt
from itertools import count, islice


def isPrime(n):
    if n < 2 or n % 2 == 0:
        return False
    for i in islice(count(3, 2), int(sqrt(n)-1)//2):
        if n % i == 0:
            return False
    return True


def getodd_prime(num):
    """
    Returns all odd prime no.s less than num.
    """
    num -= 2
    while num >= 3:
        if isPrime(num):
            yield num
        num -= 2


def conjecture(num):
    """
    Parameter
    ---------
    num : int
    """
    if isPrime(num):
        return True
    odds = getodd_prime(num)
    n = num
    while n > 3:
        try:
            prime = next(odds)
            if (num - prime) % 2 == 0:
                diff = (num - prime)/2
                if sqrt(diff) == int(sqrt(diff)):
                    return True
            n -= 2
        except:
            break
    return False

if __name__ == '__main__':
    num = 33
    while conjecture(num):
        num += 2
    print num
