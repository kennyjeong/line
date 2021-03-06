#!/usr/bin/python3
#Day 27 Problem solving, coming from https://www.hackerrank.com/challenges/two-strings/

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    char_s2 = []
    char_s2[:]=s2
    for i in range(0, len(char_s2)):
        if char_s2[i] in s1:
            return "YES"
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

