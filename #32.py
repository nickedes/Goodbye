def check_pandigital(string, s=9):
    string = str(string)
    return len(string) == s and not '1234567890'[:s].strip(string)

pandigital = set()
for i in range(2, 60):
    if i < 10:
        start = 1234
    else:
        start = 123
    for j in range(start, 10000//i):
        string = str(i)+str(j)+str(i*j)
        if check_pandigital(string):
            pandigital.add(i*j)

print sum(pandigital)
