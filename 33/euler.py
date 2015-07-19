# Logic:
# For each potential fraction (10..99 / 10..99 )
#     If the num or denom are mod 10, skip it
#     if the num and denom share a common digit
#         divide num and denom and store the result in 'expected'
#         remove the common digit from num and denom (generating num' and denom')
#         divide num' and denom' and compare the result to 'expected'
#         if the results match then I have found one of the four answers
#     next
# Multiply the four fractions
# Report the denominator in lowest common terms to the website
d = 1
for i in range(10, 100):
    for j in range(i, 100):
        if i % 10 == 0 or j % 10 == 0:
            continue
        if i == j:
            continue
        if str(i)[0] == str(j)[0]:
            if i/float(j) == int(str(i)[-1])/float(int(str(j)[-1])):
                d *= i/float(j)
        elif str(i)[0] == str(j)[-1]:
            if i/float(j) == int(str(i)[-1])/float(int(str(j)[0])):
                d *= i/float(j)
        elif str(i)[-1] == str(j)[0]:
            if i/float(j) == int(str(i)[0])/float(int(str(j)[-1])):
                d *= i/float(j)
        elif str(i)[-1] == str(j)[-1]:
            if i/float(j) == int(str(i)[0])/float(int(str(j)[0])):
                d *= i/float(j)
        else:
            continue
print 1/d
# d = 1
# for i in range(1, 10):
#     for j in range(1, i):
#         q, r = divmod(9*j*i, 10*j-i)
#         if not r and q <= 9:
#             d *= i/float(j)
# print d
