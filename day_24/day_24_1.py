#!/usr/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = count_ex = 0;
    str_len = len(s)
    for i in range(0,str_len):
        if s[i] == "a":
            count+=1
    count = count * int(n/str_len)

    for i in range(0, n%str_len):
        if s[i] == "a":
            count_ex+=1

    return count+count_ex

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

