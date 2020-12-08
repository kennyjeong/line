#!/usr/bin/python3
# 8th day Extra solving, the problem is coming from https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/


import sys

S = input().strip()
try:
    nVal = int(S)
    print(nVal)
except ValueError:
    print("Bad String")
