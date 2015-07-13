from time import time
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

target = int(raw_input('Enter N: '))
start = time()
coins = [1, 2, 5, 10, 20, 50, 100, 200]
print count(coins,len(coins),target)%(10**9+7), time()-start