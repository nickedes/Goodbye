import sys
inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    n = int(next(inputs))
    a = []
    for j in range(n): 
        k = next(inputs)
        if j < n-1:
            k = k[:-1]
        k = k.split(' ')
        a.append(k)
    for row in range(len(a)):
        for col in range(len(a[row])):
            a[row][col] = int(a[row][col])
    row = len(a) - 2
    while row >= 0:
        for i in range(len(a[row])):
            a[row][i] += max(a[row+1][i],a[row+1][i+1])
        row -= 1
    print a[0][0]