#!/usr/bin/python3
#Day 25 Problem Solving, Coming from https://www.hackerrank.com/challenges/pairs

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    myDict = {item : 1 for index, item in enumerate(arr)}
    count = 0
    for each in myDict:
        if each + k in myDict:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

