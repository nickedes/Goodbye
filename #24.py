from itertools import permutations

all = permutations(range(10))
list_of_perm = []
for permutation in all:
	 number = int("".join(str(i) for i in permutation))
	 list_of_perm.append(number)

list_of_perm.sort()
print list_of_perm[pow(10,6)-1]