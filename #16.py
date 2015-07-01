import sys
inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    n = int(next(inputs))
    sum_dig = 0
    for x in str(pow(2,n)):
        sum_dig +=int(x)
    print sum_dig