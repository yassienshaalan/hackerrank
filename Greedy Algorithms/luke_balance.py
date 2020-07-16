#!/bin/python3

import math
import os
import random
import re
import sys

#######################################
####   Problem description link #
#https://www.hackerrank.com/challenges/luck-balance/problem
#######################################

def luckBalance(k, contests):
      cont = []
      for i in range(len(contests)):
          cont.append((contests[i][0],contests[i][1]))
      cont = sorted(cont, key=lambda element: (element[0], element[1]))
      cont.reverse()
      
      luck=0
      imp_lost = 0
      for i in range(len(cont)):
          if imp_lost <k:
              if cont[i][1]==1:
                  imp_lost+=1
              luck+=cont[i][0]
          else:
              if cont[i][1]==1:
                  luck-=cont[i][0]
              else:
                  luck+=cont[i][0]
      return luck
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
