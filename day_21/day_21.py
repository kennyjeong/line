#!/usr/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()
        n = int(nk[0])
        k = int(nk[1])

        temp = result = 0
        for i in range(1, n):
            for j in range(i+1, n+1):
                result = i&j
                if result > temp and result < k:
                    temp = result

        print(temp)
