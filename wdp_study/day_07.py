#!/usr/bin/python3
#day 07 Problem solving, coming from https://www.hackerrank.com/challenges/ctci-making-anagrams
import math
import os
import random
import re
import sys

from collections import defaultdict
# Complete the makeAnagram function below.
def makeAnagram(a, b):
    da = defaultdict(int)
    for e in a:
        da[e]+= 1
    for e in b:
        da[e]-= 1
return  sum([abs(e) for e in da.values()])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

