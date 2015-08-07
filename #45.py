def isPentagonal(num):
    """
    """
    pass


def isHexagonal(num):
    """
    """
    pass


def findTriangular():
    """
    """
    term = 285
    while True:
        term += 1
        triang = term*(term+1)/2
        if isPentagonal(triang) and isHexagonal(triang):
            print triang
            break
    pass
