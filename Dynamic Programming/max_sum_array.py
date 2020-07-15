#!/bin/python3

import math
import os
import random
import re
import sys

#######################################
####   Problem description link #
#https://www.hackerrank.com/challenges/max-array-sum/problem
#######################################

def maxSubsetSum(arr):
    incl = 0
    excl = 0
    for i in range(len(arr)): 
        # Current max excluding i (No ternary) 
        new_excl = max(excl,incl)
        # Current max including i 
        incl = excl + arr[i] 
        excl = new_excl 
    # return max of incl and excl 
    return max(excl,incl) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
