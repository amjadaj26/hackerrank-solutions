#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Write your code here
    my_set = set()
    counter = 0
    valueofarr = 0
    for i in arr:
        my_set.add(i)
    for j in my_set:
        if (valueofarr < j and counter < arr.count(j) ):
            counter = arr.count(j)
            valueofarr = j
    return valueofarr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
