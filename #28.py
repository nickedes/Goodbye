import sys
inputs = sys.stdin
t = int(next(inputs))
for x in xrange(t):
    L = int(next(inputs))
    n = (L-1) // 2
    sum_d = (16*n**3 + 30*n**2 + 26*n + 3) // 3
    print sum_d % (10**9+7)