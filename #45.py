from math import sqrt


def isPentagonal(num):
    """Checks if the given number is a Pentagonal number or not."""
    n = (1 + sqrt(1 + 24*num))/6
    if int(n) == n:
        return True
    return False


def isHexagonal(num):
    """Checks if the given number is a Hexagonal number or not."""
    n = (1 + sqrt(1 + 8*num))/4
    if int(n) == n:
        return True
    return False


def findTriangular():
    """
    Finds the triangular number which is Pentagonal and Hexagonal.
    """
    term = 285
    while True:
        term += 1
        triang = term*(term+1)/2
        if isPentagonal(triang) and isHexagonal(triang):
            return triang


print findTriangular()
