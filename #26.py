from itertools import islice,count
from math import sqrt
from time import time
def isPrime(n):
    if n < 2: return False
    for i in islice(count(3,2), int(sqrt(n)-1)//2):
        if n%i ==0:
            return False
    return True

l = int(raw_input('l'))
start = time()
if l%2 != 0:
	l += 1
for d in xrange(l-1,1,-2):
	if d == 5:
		pass
	elif isPrime(d):
		power = 1
		while pow(10,power,d) != 1:
			power += 1
		if d-1 == power:
			break

print d,time()-start