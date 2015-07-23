n = int(raw_input("N"))
k = int(raw_input("k"))
d = 1
for i in range(10**(n-1), 10**n):
    for j in range(i, 10**n):
        num = i
        den = j
        if num % 10 == 0 or den % 10 == 0:
            continue
        if num == den:
            continue
        if str(num)[0] == str(den)[0]:
            if num/float(den) == int(str(num)[-1])/float(int(str(den)[-1])):
                d *= num/float(den)
        elif str(num)[0] == str(den)[-1]:
            if num/float(den) == int(str(num)[-1])/float(int(str(den)[0])):
                d *= num/float(den)
        elif str(num)[-1] == str(den)[0]:
            if num/float(den) == int(str(num)[0])/float(int(str(den)[-1])):
                d *= num/float(den)
        elif str(num)[-1] == str(den)[-1]:
            if num/float(den) == int(str(num)[0])/float(int(str(den)[0])):
                d *= num/float(den)
        else:
            continue
print 1/d
