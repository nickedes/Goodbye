import sys

def egcd(a, b):
    "To find gcd of two numbers."
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    n = int(next(inputs))
    i,res = 1,2
    while res <= n:
        if i % res != 0:
            gcd, _, _ = egcd(i,res)
            i = i*res/gcd
        res += 1
    print i