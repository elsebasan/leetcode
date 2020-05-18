#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    total_pair = 0
    dict_socks = {}
    for sock in ar:
        if sock in dict_socks:
            total_pair = total_pair + 1
            dict_socks.pop(sock)
        else:
            dict_socks[sock] = 1
    return total_pair
            
        
        

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 9
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
    result = sockMerchant(n, ar)
    assert result == 3

    n = 10
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20, 50]
    result = sockMerchant(n, ar)
    assert result == 4

    n = 0
    ar = []
    result = sockMerchant(n, ar)
    assert result == 0






