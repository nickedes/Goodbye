from math import sqrt
from itertools import count, islice


def allRot(num):
    # Gives all rotation for this num.
    rotations = []
    for n in range(len(num)):
        rotations.append(num[n:]+num[:n])
    return rotations


def isPrime(num_list):
    for num in num_list:
        n = int(num)
        if n < 2 or n % 2 == 0:
            return False
        for i in islice(count(3, 2), int(sqrt(n)-1)//2):
            if n % i == 0:
                return False
    return True

counter = 1
for num in xrange(3, 10**6, 2):
    if isPrime(allRot(str(num))):
        counter += 1

print counter
