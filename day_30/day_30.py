#!/bin/python3
#Day 30 Problem solving, coming from https://www.hackerrank.com/challenges/frequency-queries/
import math
import os
import random
import re
import sys

# Complete the freqQuery function below.
def freqQuery(queries):
    results = []
    lookup = dict()
    freq_dict = defaultdict(set)
    for command, value in queries:
        freq = lookup.get(value, 0)
        if command == 1:
            lookup[value] = freq + 1
            freq_dict[freq].discard(value)
            freq_dict[freq + 1].add(value)
        elif command == 2:
            lookup[value] = max(0, freq - 1)
            freq_dict[freq].discard(value)
            freq_dict[freq - 1].add(value)
        elif command == 3:
            results.append(1 if freq_dict[value] else 0)
    return results

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

