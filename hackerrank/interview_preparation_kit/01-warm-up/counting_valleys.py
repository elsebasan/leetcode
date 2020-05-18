#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    position = 0
    valleys = 0
    for direction in s:
        if direction == 'U':
            position = position + 1
        else:
            position = position - 1

        if position == 0 and direction == 'U':
            valleys = valleys + 1
    return valleys


if __name__ == '__main__':

    n = 8
    s = "UDDDUDUU"
    result = countingValleys(n, s)
    assert result == 1

    n = 2
    s = "UD"
    result = countingValleys(n, s)
    assert result == 0

    n = 0
    s = ""
    result = countingValleys(n, s)
    assert result == 0

    n = 2
    s = "DU"
    result = countingValleys(n, s)
    assert result == 1

    n = 6
    s = "DUDUDU"
    result = countingValleys(n, s)
    assert result == 3

    n = 8
    s = "DUUUDDDU"
    result = countingValleys(n, s)
    assert result == 2

