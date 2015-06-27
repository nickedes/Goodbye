import sys
import textwrap
inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    n = int(next(inputs))
    k = int(next(inputs))
    num = int(next(inputs))
    prod = 1
    textnum = textwrap.wrap(str(num), k)
    for part in textnum:
        tmp = 1
        for j in range(len(part)):
            tmp *= int(part[j])
        if tmp > prod: prod = tmp
    print prod