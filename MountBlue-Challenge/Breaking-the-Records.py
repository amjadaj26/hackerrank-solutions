#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    
    min_count = 0
    max_count = 0
    max_score = scores[0]
    min_score = scores[0]
    length = len(scores)
    for i in range(1,length):
        if (scores[i] > max_score):
            max_count += 1
            max_score = scores[i]
        elif (scores[i] < min_score):
            min_count += 1
            min_score = scores[i]
        else:
            continue
        
    arr = [max_count,min_count]
    return arr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
