
Facs = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def sum_Fac_digits(num):
    sum_dig_fac = 0
    for x in str(num):
        sum_dig_fac += Facs[int(x)]
    return sum_dig_fac

sum_ = 0
for i in range(3, 50000):
    if i == sum_Fac_digits(i):
        sum_ += i

print sum_
