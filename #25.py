import sys
inputs = sys.stdin
t = int(next(inputs))
for x in xrange(t):
    n = int(next(inputs))
    a,b=1,1
    digit = 1
    index = 1
    while digit:
        if len(str(a)) == n:
            print index
            digit = 0
        else:
            c = a + b
            a = b
            b = c
            index += 1
