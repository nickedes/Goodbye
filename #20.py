import sys
inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    n = int(next(inputs))
    fac = 1
    for x in xrange(2,n+1):
        fac *= x
    print sum([int(dig) for dig in str(fac)])
