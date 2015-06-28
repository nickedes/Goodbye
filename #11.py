import sys
inputs = sys.stdin
mat = [] 
for i in range(20):
    mat.append([])
    if i <19:row = next(inputs)[:-1].split(' ')
    else:row = next(inputs).split(' ')
    for j in row: mat[i].append(int(j))
prod = 0
for j in range(20):
    for k in range(16):
        tmp = mat[j][k]*mat[j][k+1]*mat[j][k+2]*mat[j][k+3]
        if tmp > prod: prod = tmp
        tmp = mat[k][j]*mat[k+1][j]*mat[k+2][j]*mat[k+3][j]
        if tmp > prod: prod = tmp
for j in range(16):
    for k in range(16):
        tmp = mat[j][k]*mat[j+1][k+1]*mat[j+2][k+2]*mat[j+3][k+3]
        if tmp > prod: prod = tmp
for j in range(3,20):
    for k in range(16):
        tmp = mat[j][k]*mat[j-1][k+1]*mat[j-2][k+2]*mat[j-3][k+3]
        if tmp > prod: prod = tmp
print prod