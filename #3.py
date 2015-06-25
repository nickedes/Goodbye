import sys
from math import sqrt

# take input from stdin
inputs=sys.stdin
# no. of test cases.
t = int(next(inputs))

for i in range(t):
    n = int(next(inputs))
    # List of prime factors
    pf = []
    if n%2 == 0:
        pf.append(2)
    while n%2 == 0:
        n = n/2
    for i in range(3,int(sqrt(n))+1,2):
        if n%i == 0:
            pf.append(i)
        while n%i == 0:
            n = n/i
    if n > 2:
        pf.append(n)
    print max(pf)