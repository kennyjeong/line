#!/usr/bin/python3
#Day 10 Problem solving, coming from https://www.hackerrank.com/challenges/special-palindrome-again

import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):

    count = n

    seq3, seq3_c = 0, ""
    seq2, seq2_c = 0, ""
    seq1, seq1_c = 1, s[0]

    for i, char in enumerate(s[1:]):
        if char == s[i]:
            count += seq1
            seq1 += 1
        else:
            seq3, seq3_c = seq2, seq2_c
            seq2, seq2_c = seq1, seq1_c
            seq1, seq1_c = 1, char

        if seq2 == 1 and seq3 >= seq1 and seq3_c == seq1_c:
            count += 1

    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()

