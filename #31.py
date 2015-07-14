import sys
def count(S, m, n):
    """
        S -> A list of coins
        m -> No. of coins
        n -> Target coin 
    """
    Matrix = [1]+[0]*n
    for coin in S:
        for i in range(coin, n+1):
            Matrix[i] += Matrix[i-coin]
    return Matrix[n]
inputs=sys.stdin
t = int(next(inputs))
coins = [1, 2, 5, 10, 20, 50, 100, 200]
results = {}
for i in xrange(t):
    target = int(next(inputs))
    if target in results:
        print results[target]
    else:
        results[target] = count(coins,len(coins),target)%(10**9+7)
        print results[target]