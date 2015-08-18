from math import sqrt


def sieve(limit):
    """Computes the sieve of Eratosthenes for values up to limit included."""
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(sqrt(limit)) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes


def sum_primes():
    """
    """
    limit = 1000000
    primes = sieve(limit)
    list_primes = [i for i, p in enumerate(primes) if p]
    max_len, max_sum = 0, 0
    for i in range(len(list_primes)):
        for j in range(i + max_len + 1, len(list_primes)):
            s = sum(list_primes[i:j])  # could use sum array here
            if s > limit:
                break
            elif primes[s]:
                assert j - i > max_len
                max_len, max_sum = j - i, s
    return max_sum


if __name__ == '__main__':
    print sum_primes()
