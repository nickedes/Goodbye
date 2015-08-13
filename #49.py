from itertools import permutations, count, islice
from math import sqrt


def isPrime(n):
    if n < 2 or n % 2 == 0:
        return False
    for i in islice(count(3, 2), int(sqrt(n)-1)//2):
        if n % i == 0:
            return False
    return True


def getPerm(num):
    """
    """
    return permutations(num)


def getPrimes():
    """
    """
    list_primes = []
    for num in range(1000, 10000):
        if isPrime(num):
            list_primes.append(num)
    return list_primes


def Prime_permutations():
    """
    """
    all_primes = getPrimes()
    first, second, third = 0, 0, 0
    for index in range(len(all_primes)):
        first = all_primes[index]
        if first != 1487:
            second, third = first + 3330, first + 6660
            if sorted(set(str(first))) == sorted(set(str(second))) and \
                    sorted(set(str(second))) == sorted(set(str(third))):
                if second in all_primes and third in all_primes:
                    return str(first) + str(second) + str(third)


print(Prime_permutations())
