import sys
inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    if t == 1:
        m,n = next(inputs).split(' ')
        m,n=int(m)+1,int(n)+1
    elif i == 0:
        m,n = next(inputs).split(' ')
        m,n = int(m)+1,int(n[:-1])+1
    else:
        m,n = next(inputs).split(' ')
        m,n=int(m)+1,int(n)+1
    path = [[0]*n for _ in xrange(m)]
    for i in xrange(m):
        path[i][0] = 1
    for j in xrange(n):
        path[0][j] = 1

    for i in xrange(1,m):
        for j in xrange(1,n):
            path[i][j] = path[i-1][j] + path[i][j-1]

    print path[m-1][n-1]%(pow(10,9)+7)
