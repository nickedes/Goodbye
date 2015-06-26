import sys

def findpal(n):
    pals,i = 0,999
    while i > 99:
        j = 999
        while j >= i:
            prod = i*j
            j = j-1
            if prod < pals:
                break
            if str(prod)==(str(prod)[::-1]) and prod < n:
                if prod > pals:
                    pals = prod
            
        i = i-1
    return pals
inputs = sys.stdin
t = int(next(inputs))

for i in range(t):
    n = int(next(inputs))
    print findpal(n)