from math import sqrt


def wordValue(word):
    """Calculate the word value.

    Converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value.
    """
    val = 0
    for alpha in word[1:len(word)-1]:
        val += ord(alpha)-64
    return val


def isTriangular(val):
    """
    val -- word value
    n -- nth term
    """
    n = (sqrt(1+8*val)-1)/2
    if int(n) == n:
        return True
    return False


with open('p042_words.txt') as f:
    all_words = f.read().split(",")
    count = 0
    for word in all_words:
        # Calculate the value of word and if it's triangular!
        if isTriangular(wordValue(word)):
            count += 1
    print count
