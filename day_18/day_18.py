#!/usr/bin/python3
#Day 18 Problem solving, coming from https://www.hackerrank.com/challenges/30-nested-logic/problem
day={}
month={}
year={}
line=input().split()
day[0]=int(line[0])
month[0]=int(line[1])
year[0]=int(line[2])
line=input().split()
day[1]=int(line[0])
month[1]=int(line[1])
year[1]=int(line[2])

#Select Mode Mode:0 in this year,
fine = 0
if year[0] > year[1]:
    fine=10000
elif year[0] == year[1]:
    if month[0] > month[1]:
        fine=(month[0]-month[1])*500
    elif month[0] == month[1]:
        if day[0] > day[1]:
            fine=(day[0]-day[1])*15

print(fine)
