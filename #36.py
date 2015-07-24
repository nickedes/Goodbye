sum_ = 0
for num in xrange(10**6):
    # If Palindrome in base-10 and base-2
    binary = bin(num)[2:]
    if str(num) == str(num)[::-1] and binary == binary[::-1]:
        sum_ += num

print sum_
