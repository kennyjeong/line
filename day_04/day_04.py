#!/usr/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max = 0
    for i in range(0,4,1):
        temp = 0
        for j in range(0,4,1):
            temp=arr[i][j]+arr[i+1][j]+arr[i+2][j]
            temp+=arr[i][j+1]+arr[i+1][j+1]+arr[i+2][j+1]
            temp+=arr[i][j+2]+arr[i+1][j+2]+arr[i+2][j+2]
            print("i:",i," j:",j,"sum=",temp,"max=",max)
            if max <= temp:
                max = temp
    print(max)



