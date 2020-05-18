
#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    lenc = len(c)
    position = 0
    while position < lenc:
        if position + 2 < lenc - 1:
            if c[position + 2] == 0:
                position = position + 2
            else:
                position = position + 1
        else:
            #end
            position = lenc
        jumps = jumps + 1
    return jumps




if __name__ == '__main__':

    n = 6
    c = [0, 0, 0, 0, 1, 0]
    result = jumpingOnClouds(c)
    assert result == 3

    n = 6
    c = [0, 1, 0, 0, 1, 0]
    result = jumpingOnClouds(c)
    assert result == 3

    n = 6
    c = [0, 0, 1, 0, 1, 0]
    result = jumpingOnClouds(c)
    assert result == 3

    n = 7
    c = [0, 0, 1, 0, 0, 1, 0 ]
    result = jumpingOnClouds(c)
    assert result == 4

    n = 11
    c = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
    result = jumpingOnClouds(c)
    assert result == 5

    n = 11
    c = [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0 ]
    result = jumpingOnClouds(c)
    assert result == 7

    n = 11
    c = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0 ]
    result = jumpingOnClouds(c)
    assert result == 6
