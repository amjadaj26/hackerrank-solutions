#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    small_alphabet = 1
    large_alphabet = 1
    special_character = 1
    number = 1
    if re.search("[a-z]",password):
        small_alphabet = 0
    if re.search("[A-Z]",password):
        large_alphabet = 0
    if re.search("[0-9]",password):
        number = 0
    if re.search("[!@#$%^&*()\\-+]",password):
        special_character = 0
    return max(6-n,small_alphabet + large_alphabet + special_character + number)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
