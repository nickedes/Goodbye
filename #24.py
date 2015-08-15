import sys


def Factor(num):
    if num < 0:
        return 0
    fac = 1
    for p in range(2, num+1):
        fac *= p
    return fac

perm = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
N = len(perm)
inputs = sys.stdin
t = int(next(inputs))
for x in xrange(t):
    num = int(next(inputs))
    permNum = []
    remain = num - 1

    numbers = []
    for i in range(N):
        numbers.append(i)

    for i in range(1, N):
        j = remain / Factor(N - i)
        remain = remain % Factor(N - i)
        permNum.append(perm[numbers[j]])
        numbers.pop(j)
        if remain == 0:
            break

    for i in range(len(numbers)):
        permNum.append(perm[numbers[i]])

    print ''.join(permNum)
