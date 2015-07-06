from itertools import permutations

all = permutations('abcdefghijklm')
dict_of_perm = {}
index = 0
done = []
for permutation in all:
	word = "".join(letter for letter in permutation)
	done.append(index)
	try:
		dict_of_perm[index] = word
		index += 1
	except:
		break
print dict_of_perm[1]
print max(done)