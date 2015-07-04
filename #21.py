import time
def sum_divisors(num):
	factors = [1]
	for i in xrange(2, num/2+1):
		if num % i == 0:
			factors.append(i)
	return sum(factors)

start = time.time()
am = []
for i in xrange(200,100000):
	num = sum_divisors(i)
	if i == sum_divisors(num) and num != i and i not in am:
		am.append(i)
		am.append(num)
print sum(am),"in",time.time()-start