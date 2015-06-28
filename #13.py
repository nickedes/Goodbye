import sys
inputs = sys.stdin
t = int(next(inputs))
sum_all = 0
for i in range(t):
    n = int(next(inputs))
    sum_all += n
print str(sum_all)[:10]