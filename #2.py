import sys
inputs=sys.stdin
t = int(next(inputs))
for i in range(t):
    n,a,b,sum = int(next(inputs)),1,2,0
    while b < n:
        if b % 2 == 0:
            sum += b
        c = a+b
        a,b = b,c
    print sum
