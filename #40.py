fraction, i = '.', 1

while True:
    fraction += str(i)
    i += 1
    if len(fraction) > 1000000:
        break

prod, index = 1, 1

while index <= 1000000:
    prod *= int(fraction[index])
    index *= 10

print prod
