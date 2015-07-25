from math import sqrt
from itertools import count, islice


def isPrime(num_list):
    for num in num_list:
        n = int(num)
        if n < 2 or n % 2 == 0 and n != 2:
            return False
        for i in islice(count(3, 2), int(sqrt(n)-1)//2):
            if n % i == 0:
                return False
    return True


def all_subs(num):
    str_num = str(num)
    all_substrings = set()
    for i in range(len(str_num)):
        all_substrings.add(str_num[i:])
        all_substrings.add(str_num[:i])
    all_substrings.remove('')
    return all_substrings

counter, sum_, num = 0, 0, 11
while counter < 11:
    if isPrime(all_subs(num)):
        sum_ += num
        counter += 1
    num += 2
print sum_
