#!/usr/bin/python3
#Day 26 Problem solving, coming from https://www.hackerrank.com/challenges/ctci-ransom-note/

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # init variable
    occurence = [0] * len(magazine)
    for i in range(0, len(note)):
        success = 0
        for j in range(0, len(magazine)):
            if occurence[j] == 0 :
                if magazine[j] == note[i] :
                    occurence[j]=1
                    success = 1
        if success == 0:
            print("No")
            return
    print("Yes")
    return


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

