#!/bin/python3

import math
import os
import random
import re
import sys



def get_text(matrix, n, m):
    text=''
    for j in range(m):
        for i in range(n):
            text += matrix[i][j]
    return text

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
text = get_text(matrix, n , m)

regex_invalid=r"(?<=\w)([^\w]+)(?=\w)"
output = re.sub(regex_invalid, " ", text)
print (output)





