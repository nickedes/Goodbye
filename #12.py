import sys
from math import sqrt
inputs = sys.stdin
t = int(next(inputs))
l = [{1:1}]
for i in range(t):
    c = int(next(inputs))
    if c==1:
        print 3
    elif c + 1 <= max(l).values()[0]:
        flag = 0
        for data in l:
            for dicta in data:
                if c+1 <= data[dicta]:
                    print dicta
                    flag = 1
                    break
            if flag == 1: break
    else:
        element =  max(l).keys()[0]
        if element == 1:
            n = 2
        else:
            n = (int(sqrt(1+4*element*2))-1)/2 + 1
        fac = 1
        num =1
        while fac < c+1:
            num = n*(n+1)/2
            fac = sum(2 for i in xrange(1, int(sqrt(num)+1)) if not num % i)
            l.append({num:fac})
            n += 1
        print max(l).keys()[0]