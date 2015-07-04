import time
import string
start = time.time()
with open('names.txt','r') as f:
	names = f.read()

a = names.split('"')

a.sort()

while ',' in a:
	a.remove(',')
while '' in a:
	a.remove('')

alphas = {}
for alpha in string.uppercase:
	alphas[alpha] = ord(alpha) - 65 + 1

score = 0
for name in a:
	ele_score = 0
	for element in name:
		ele_score += alphas[element]
	score += ele_score*(a.index(name)+1)

print score,time.time() - start