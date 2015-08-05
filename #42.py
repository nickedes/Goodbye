from math import sqrt


def wordValue(word):
    """
    """
    val = 0
    for alpha in word[1:len(word)-1]:
        val += ord(alpha)-64
    return val


def isTriangular(val):
    """
    n -- nth term
    """
    n = (sqrt(1+8*val)-1)/2
    pass


with open('p042_words.txt') as f:
    all_words = f.read().split(",")
    for word in all_words:
        # Calculate the value of word!
        value = wordValue(word)

        pass
