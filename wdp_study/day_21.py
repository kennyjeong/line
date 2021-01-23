#!/usr/bin/python3
#Day 21 Problem Solving, coming from https://www.hackerrank.com/challenges/reverse-shuffle-merge

import math
import os
import random
import re
import sys

# Complete the reverseShuffleMerge function below.
def reverseShuffleMerge(s):
    # Total character counts in s
    char_count = Counter(s)

    # Character counts we need in our final string
    string_chars = {
        char: int(count / 2) for char, count in char_count.items()
    }

    # Character counts we need in the shuffled
    # version of our original string
    shuffled_chars = {
        char: int(count / 2) for char, count in char_count.items()
    }

    string = []

    for char in reversed(s):
        if string_chars[char] > 0:
            while string and string[-1] > char and shuffled_chars[string[-1]] > 0:
                removed = string.pop()
                string_chars[removed] += 1
                shuffled_chars[removed] -= 1

            string.append(char)
            string_chars[char] -= 1
        else:
            shuffled_chars[char] -= 1

    return ''.join(string)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()

