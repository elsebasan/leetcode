import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    how_many = n // len(s)
    remainder = n % len(s)
    return s.count('a') * how_many + s[0 : remainder].count('a')





if __name__ == '__main__':

    s = "aba"
    n = 10
    result = repeatedString(s, n)
    assert result == 7

    s = "a"
    n = 1000000000000
    result = repeatedString(s, n)
    assert result == 1000000000000

