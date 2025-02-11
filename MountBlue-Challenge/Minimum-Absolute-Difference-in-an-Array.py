#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minimumAbsoluteDifference(arr):
    # Write your code here
    min_diff=[]
    arr.sort()
    for i in range(len(arr)-1):
        min_diff.append(abs(arr[i]-arr[i+1]))
    return min(min_diff)

    # or this below also work 
    # min_diff=abs(arr[0]-arr[1]) 
    # arr.sort()
    # for i in range(len(arr)-1):
    #     diff = abs(arr[i]-arr[i+1])
    #     if diff<min_diff:
    #         min_diff = diff
    # return (min_diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
