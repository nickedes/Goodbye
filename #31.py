from time import time
def count(S, m, n):
    """
        S -> A list of coins
        m -> No. of coins
        n -> Target coin 
    """
    # If n is less than 0 then no solution exists
    Matrix = [[0 for x in range(m)] for x in range(n+1)] 

    # If n is 0 then there is 1 solution (do not include any coin)
    for col in range(m):
        Matrix[0][col] = 1
 
    # If there are no coins and n is greater than 0, then no solution exist
    for row in range(1,n+1):
        Matrix[row][0] = 1        

    # count is sum of solutions (i) including S[m-1] (ii) excluding S[m-1]
    for row in range(1,n+1):
        for col in range(1,m):
            Matrix[row][col] = Matrix[row][col - 1] + Matrix[row - S[col]][col]

    return Matrix[n][m-1]

target = int(raw_input('Enter N: '))
start = time()
coins = [1, 2, 5, 10, 20, 50, 100, 200]
print count(coins,len(coins),target)%(10**9+7), time()-start