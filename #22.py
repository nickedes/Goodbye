import sys
import string
alphas = {}
for alpha in string.uppercase:
	alphas[alpha] = ord(alpha) - 65 + 1

inputs = sys.stdin
t = int(next(inputs))
names = []
for i in range(t):
    n = next(inputs)[:-1]
    names.append(n)

names.sort()
q = int(next(inputs))
for i in range(q):
    if i == q-1:
        word = next(inputs)
    else:
        word = next(inputs)[:-1]
    ele_score = 0
    for element in word:
		ele_score += alphas[element] 
    print ele_score*(names.index(word)+1)
