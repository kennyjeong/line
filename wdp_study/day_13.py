#!/usr/bin/python3
#Day 13 Problem Solving, coming from https://www.hackerrank.com/challenges/mark-and-toys
import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    count=0
    total=0
    prices.sort()
    for i in prices:
        total+=i
        if total<=k:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()

