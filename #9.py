import sys
inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    n = int(next(inputs))
    flag = 0
    prod = []
    for a in range(1, n/2):
        b = n*(n-2*a)/(2*(n-a))
        if a+b < n and pow(a, 2) + pow(b, 2) == pow(n-a-b, 2):
            flag = 1
            prod.append(a*b*(n-a-b))
    if flag == 0:
        print -1
    else:
        print max(prod)
