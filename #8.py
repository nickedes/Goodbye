import sys
inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    n, k = next(inputs)[:-1].split(' ')
    n, k = int(n), int(k)
    num = next(inputs)[:-1]
    prod = []
    textnum = []
    for u in range(len(num)):
        if len(num[u:u+k]) == k:
            textnum.append(num[u:u+k])
    for part in textnum:
        tmp = 1
        for j in range(len(part)):
            tmp *= int(part[j])
        prod.append(tmp)

    print max(prod)
