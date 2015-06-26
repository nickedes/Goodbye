import sys
inputs = sys.stdin
t = int(next(inputs))

for i in range(t):
    n = int(next(inputs))
    sum_square =  n*(n+1)*(2*n+1)/6
    sum_n = n*(n+1)/2
    square_sum = sum_n*sum_n
    print square_sum - sum_square