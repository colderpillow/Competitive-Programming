#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    cross = 0
    alt_path = []
    alt = 0
    for i in path:
        if i == 'U':
            alt +=1
            alt_path.append(alt)
        elif i == 'D':
            alt -= 1
            alt_path.append(alt)
    for i in range(len(alt_path)):
        if alt_path[i] == -1 and alt_path[i+1] == 0:
            cross += 1
    return(cross)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
