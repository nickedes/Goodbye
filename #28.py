sum_diag, d, L = 1, 1, 1001
for n in range(2, L, 2):
    sum_diag += 4*d + 10*n
    d += 4*n;
print sum_diag