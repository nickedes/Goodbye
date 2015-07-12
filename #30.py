import sys
inputs = sys.stdin
digit = int(next(inputs))
num = 10
pos = []
#  9^n x (n-1) is actually more than adequate, which reduces the search range
#  and improves the performance of the program.
maximum = 9**digit * (digit-1)
while num < maximum:
    n = num
    test = 0
    while n > 0:
        test += pow(n % 10, digit)
        n = n/10
    if num == test:
        pos.append(num)
    num += 1
print sum(pos)
