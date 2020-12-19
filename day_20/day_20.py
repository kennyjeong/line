#!/usr/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

emailList=[]
for N_itr in range(N):
    firstNameEmailID = input().split()
    firstName = firstNameEmailID[0]
    emailID = firstNameEmailID[1]
    emailID = emailID.split("@")
    if emailID[1] == "gmail.com":
        emailList.append(firstName)

emailList.sort()
for i in range(len(emailList)):
    print(emailList[i])
