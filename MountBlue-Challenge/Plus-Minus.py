#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    count_zero=0
    count_pos=0
    count_neg=0
    for i in arr:
        if i > 0:
            count_pos+=1
        elif(i < 0):
            count_neg+=1
        else:
            count_zero+=1
    print(format(count_pos/n,'.6f'))
    print(format(count_neg/n,'.6f'))
    print(format(count_zero/n,'.6f'))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
