import time
from itertools import count,islice
start = time.time()
 
def collatz(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n/2
            if n > 1:
                count += 1
                if n % 2 == 0:
                    n = n/2
                else:
                    n = 3*n + 1
        else:
            n = 3*n + 1
            if n > 1:
                count += 1
                if n % 2 == 0:
                    n = n/2
                else:
                    n = 3*n + 1
    return count
 
max = [0,0]
for i in islice(count(2),0,1000000-1):
    c = collatz(i)
    if c > max[0]:
        max[0] = c
        max[1] = i
 
elapsed = (time.time() - start)
print "found %s at length %s in %s seconds" % (max[1],max[0],elapsed)