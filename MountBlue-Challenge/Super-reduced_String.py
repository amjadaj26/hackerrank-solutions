#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def superReducedString(s):
    # Write your code here
    stack=[] #initialise a stack 
    for i in s:
        if stack and stack[-1]==i: #if stack is not empty and top element of stack is i from string
            stack.pop() #remove the top element and do not insert anything
        else:
            stack.append(i) #else insert the element
        #this way there will be no duplicate values in the stack
    if stack:
        return ''.join(stack)
    else:
        return 'Empty String'
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
