# key: perimeter
# value: no. of solutions
peri_dicts = {}

# sides : a, b, c of triangle
for n in xrange(120, 1001):
    peri_dicts[n] = 0
    for a in xrange(1, n/3):
        b = n*(n-2*a)/(2*(n-a))
        if a+b < n and pow(a, 2) + pow(b, 2) == pow(n-a-b, 2):
            peri_dicts[n] += 1

max_val = max(peri_dicts.values())
for key, value in peri_dicts.items():
    if value == max_val:
        print key
