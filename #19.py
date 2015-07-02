import sys
from math import floor

def day_of_week(year, month, day):
    d = day
    m = (month - 3) % 12 + 1
    if m > 10: Y = year - 1
    else: Y = year
    y = Y % 100
    c = (Y - (Y % 100)) / 100
 
    w = (d + floor(2.6 * m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7
 
    return int(w)

def months_start_range(day,year_start,year_end):
    total = 0
    for year in range(year_start, year_end + 1):
        for month in range(1,13):
            if day_of_week(year, month, 1) == day: total += 1
    return total

inputs = sys.stdin
t = int(next(inputs))
for i in range(t):
    if i != t-1:
        y1,m1,d1 = next(inputs)[:-1].split(' ')
        y2,m2,d2 = next(inputs)[:-1].split(' ')
    else:
        y1,m1,d1 = next(inputs)[:-1].split(' ')
        y2,m2,d2 = next(inputs).split(' ')
    y1,m1,d1 = int(y1),int(m1),int(d1)
    y2,m2,d2 = int(y2),int(m2),int(d2)
    if y2 >= y1:
        total = 0
        if m1 > 1: 
            total = months_start_range(0,y1+1,y2-1)
            for i in range(m1,13):
                if day_of_week(y1, i, 1) == 0: total += 1
        else:
            total = months_start_range(0,y1,y2-1)
        for i in range(1,m2+1):
            if day_of_week(y2, i, 1) == 0: total += 1
        print total
    else:
        print 0