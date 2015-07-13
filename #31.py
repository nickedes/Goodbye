from time import time
def count(S, m, n):
    """
        S -> A list of coins
        m -> No. of coins
        n -> Target coin 
    """

    # If n is 0 then there is 1 solution (do not include any coin)
    if n == 0:
        return 1
     
    # If n is less than 0 then no solution exists
    if n < 0:
        return 0
 
    # If there are no coins and n is greater than 0, then no solution exist
    if m <= 0 and n >= 1:
        return 0

    # count is sum of solutions (i) including S[m-1] (ii) excluding S[m-1]
    return count( S, m - 1, n ) + count( S, m, n-S[m-1] )

start = time()
coins = [1, 2, 5, 10, 20, 50, 100, 200]
print count(coins,len(coins),200), time()-start