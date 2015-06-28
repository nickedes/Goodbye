import sys
inputs = sys.stdin
mat = [] 
for i in range(20):
    mat.append([])
    if i <19:row = next(inputs)[:-1].split(' ')
    else:row = next(inputs).split(' ')
    for j in row: mat[i].append(int(j))
maxp = 0
for i in range(20):
    for j in range(17):
        up_down = max(mat[i][j] * mat[i][j+1] * mat[i][j+2] * mat[i][j+3],
                  mat[j][i] * mat[j+1][i] * mat[j+2][i] * mat[j+3][i])
        if i < 16:
            diag = max(mat[i][j] * mat[i+1][j+1] * mat[i+2][j+2] * mat[i+3][j+3],
                     mat[i][j+3] * mat[i+1][j+2] * mat[i+2][j+1] * mat[i+3][j])
        maxp = max(maxp, up_down, diag)
print maxp