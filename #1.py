# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
inputs=sys.stdin
t = int(next(inputs))
for i in range(t):
    n = int(next(inputs))
    three,five,both = 0,0,0
    if n%3 == 0:
        three = n/3 - 1
    else:
        three = n/3 
    if n%5 == 0:
        five = n/5 - 1
    else:
        five = n/5
    if n%15 == 0:
        both = n/15 - 1
    else:
        both = n/15
    print 3*three*(three+1)/2 + 5*five*(five+1)/2 - 15*both*(both+1)/2
