import time
start = time.time()
m,n = 21,21
path = [[0]*n for _ in xrange(m)]
for i in xrange(m):
	path[i][0] = 1
for j in xrange(n):
	path[0][j] = 1

for i in xrange(1,m):
	for j in xrange(1,n):
		path[i][j] = path[i-1][j] + path[i][j-1]

print path[m-1][n-1]
print time.time() - start