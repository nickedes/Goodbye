ncr_map = dict()

def NCR(n, r):
	global ncr_map
	if n == r or r == 0:
		return 1
	if (n, n - r) in ncr_map:
		return ncr_map[ (n, n - r) ]
	if (n, r) in ncr_map:
		return ncr_map[ (n, r) ]
	value = NCR(n-1, r-1) + NCR(n - 1, r)
	ncr_map[ (n, r) ] = value
	return value


count = 0
for n in range(1, 101):
	print(n)
	for r in range(1, n + 1):
		ncr = NCR(n, r)
		if ncr > 1000000:
			count+=1

print(count)