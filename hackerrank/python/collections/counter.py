#!/usr/bin/env python

import itertools
from collections import Counter


x_var = int(input())
if 0 < x_var < 10000:
    dic_shoes = Counter(list(map(int, input().split( ))))
    print(dic_shoes)
    number_customers = int(input())
    for _ in itertools.repeat(None, number_customers):
        size, price =


exit(0)