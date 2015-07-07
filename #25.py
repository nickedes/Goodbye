a,b=1,1
digit = 1
index = 1
n = 1000
while digit:
	if len(str(a)) == n:
		print index
		digit = 0
	else:
		c = a + b
		a = b
		b = c
		index += 1

print 'done!'