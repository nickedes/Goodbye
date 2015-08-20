"""
If the fixed number is 2 digit we wont be able to generate a 9 digit number
since n = 3 yields an 8 digit number and n=4 yields an 11 digit number.
Same goes for 3 digit numbers where we end at 7 or 11 digits in the result.
That leaves us with a four digit number starting with 9.
"""


def check_pandigital(string, s=9):
    """
    Checks if the passed `string` is pandigital or not.
    """
    return len(string) == s and not '1234567890'[:s].strip(string)


def largest():
    """
    Gives the largest pandigital number.
    """
    max_pan = 918273645
    for x in range(9123, 9999+1):
        possible_pan = str(x) + str(x*2)
        if check_pandigital(possible_pan) and int(possible_pan) > max_pan:
            max_pan = int(possible_pan)
    return max_pan


print(largest())
