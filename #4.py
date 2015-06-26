pal = []
def checkPal(number):
    num = number
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev*10 + dig
        num /= 10
    if rev == number:
        return 1
    return 0

def findpal():
    maxpal=0
    for i in range(999,900,-1):
        for j in range(999,900,-1):
            prod = i*j
            if checkPal(prod):
                if maxpal < prod:
                    maxpal = prod
    return maxpal
print findpal()