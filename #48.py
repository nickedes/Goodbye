def _sum(num):
    """
    Returns the sum of numbers upto `num`.
    """
    x = 0
    for i in range(1, num+1):
        x += i**i
    return x

# Prints last 10 digits of the sum.
print str(_sum(1000))[-10:]
