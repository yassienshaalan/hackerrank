#!/bin/python3

import math
import os
import random
import re
import sys

#######################################
####   Problem description link #
#https://www.hackerrank.com/challenges/ctci-ransom-note/problem
#######################################
def checkMagazine(magazine, note):

    mag_dict = dict()
    for i in range(len(magazine)):
        try:
            result = mag_dict[magazine[i]]
            result+=1
            mag_dict[magazine[i]]=result
        except KeyError:
            mag_dict[magazine[i]]=0
    
    note_dict = dict()
    for i in range(len(note)):
        try:
            result = note_dict[note[i]]
            result+=1
            note_dict[note[i]]=result
        except KeyError:
            note_dict[note[i]]=0

    result = "Yes"
    for key,val in note_dict.items():
        try:
            if mag_dict[key]<val:
                result="No"
                break
        except KeyError:
            result="No"
            break
   #print("result",result)
    return result
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
