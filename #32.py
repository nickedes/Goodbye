import sys


def check_pandigital(string, s=9):
    string = str(string)
    return len(string) == s and not '1234567890'[:s].strip(string)

inputs = sys.stdin
n = int(next(inputs))
pandigital = set()
if n > 7:
    for i in range(2, 60):
        if i < 10:
            start = 1234
        else:
            start = 123
        for j in range(start, 10000//i):
            string = str(i)+str(j)+str(i*j)
            if check_pandigital(string, n):
                pandigital.add(i*j)
else:
    pandigital = set()
    for i in range(1, 10):
        for j in range(1000):
            string = str(i)+str(j)+str(i*j)
            if check_pandigital(string, n):
                pandigital.add(i*j)
print sum(pandigital)
