from itertools import permutations


def getPerm():
    """Get all the permutations of 0-9"""
    return permutations(range(10))
    pass


def substring_divisible(pandigital):
    """
    Check substring divisiblity as per problem statement here
    https://projecteuler.net/problem=43
    """
    Prime_list = [2, 3, 5, 7, 11, 13, 17]
    for x in range(1, len(pandigital)-2):
        if int(pandigital[x:x+3]) % Prime_list[x-1] != 0:
            return False
    return True


def sumall():
    """
    Calculate sum of all 0-9 pandigital no.s with substring divisiblity.
    """
    # all perms
    perms = getPerm()
    count = 0
    while True:
        try:
            # Get next permutation from generator!
            next_permutation = next(perms)
            num = ''.join(str(x) for x in next_permutation)
            if substring_divisible(num):
                count += int(num)
        except:
            return count

print sumall()
