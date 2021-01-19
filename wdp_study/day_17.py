#!/usr/bin/python3
#Day 17 Problem Solving, coming from https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    min_abs = min((abs(arr[i] - arr[i-1]) for i in range(1, len(arr))))
    s = set()
    for x in arr:
        if x in s:
            return 0
        for d in range(1, min_abs):
            if x + d in s or x - d in s:
                min_abs = d
                break
        s.add(x)
    return min_abs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

