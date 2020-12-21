#!/usr/bin/python3
#Day 22 Problem Solving, coming from https://www.hackerrank.com/challenges/
import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    story = 0
    vally = 0
    for i in range (0, steps):
        if path[i] == "U":
            story+=1
        elif path[i] == "D":
            story-=1

        if story == 0 and path[i]=="U":
            vally += 1
    return vally
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

