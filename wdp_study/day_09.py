#!/usr/bin/python3
#Day_09 Problem Solving, coming from https://www.hackerrank.com/challenges/sherlock-and-valid-string

import math
import os
import random
import re
import sys

# Complete the isValid function below.
from collections import Counter
def isValid(s):
    C = Counter(s) ; V = list(C.values())
    F = Counter(V)

    if len(F) == 1 : return "YES"
    if len(F) > 2 : return "NO"

    if F[1] == 1 : return "YES"
    m, M = min(V), max(V)
    return "YES" if F[M] == 1 and M == m+1 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

