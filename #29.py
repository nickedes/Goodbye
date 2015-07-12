n = 100
seq = []
for a in xrange(2, n+1):
    for b in xrange(2, n+1):
        if pow(a, b) not in seq:
            seq.append(pow(a, b))

print len(seq)
