import time
from math import floor
 
"""
Gaussian algorithm to determine day of week
"""
def day_of_week(year, month, day):
    """
    w = (d+floor(2.6*m-0.2)+y+floor(y/4)+floor(c/4)-2*c) mod 7
 
    Y = year - 1 for January or February
    Y = year for other months
    d = day (1 to 31)
    m = shifted month (March = 1, February = 12)
    y = last two digits of Y
    c = first two digits of Y
    w = day of week (Sunday = 0, Saturday = 6)
    """
 
    d = day
    m = (month - 3) % 12 + 1
    if m > 10: Y = year - 1
    else: Y = year
    y = Y % 100
    c = (Y - (Y % 100)) / 100
 
    w = (d + floor(2.6 * m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7
 
    return int(w)
 
"""
Compute the number of months starting on a given day of the week in a century
"""
def months_start_range(day,year_start,year_end):
    total = 0
    for year in range(year_start, year_end + 1):
        for month in range(1,13):
            if day_of_week(year, month, 1) == day: total += 1
    return total
 

y1 = int(raw_input("y1"))
m1 = int(raw_input("m1"))
d1 = int(raw_input("d1"))
y2 = int(raw_input("y2"))
m2 = int(raw_input("m2"))
d2 = int(raw_input("d2"))

start = time.time()
if m1 > 1: 
    total = months_start_range(0,y1+1,y2-1)
else:
    total = months_start_range(0,y1+1,y2-1)

for i in range(m1,13):
    if day_of_week(y1, i, 1) == 0: total += 1

for i in range(1,m2+1):
    if day_of_week(y1, i, 1) == 0: total += 1
elapsed = time.time() - start
 
print("%s found in %s seconds") % (total,elapsed)