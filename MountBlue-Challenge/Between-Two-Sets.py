#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    count=0
    for i in range(min(a),max(b)+1):
        if (all([i%loopofa == 0 for loopofa in a]) and all([loopofb%i == 0 for loopofb in b])):
            count+=1
        else:
            continue
    return count

#for the visitors :)
#The all() function returns True if all items in an iterable are true, otherwise it returns False.
#If the iterable object is empty, the all() function also returns True.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
