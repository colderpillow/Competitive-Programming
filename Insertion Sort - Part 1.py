#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    num = arr[-1]
    
    for i in range(1,len(arr)):
        if arr[-i-1] > num:
            arr[-i] = arr[-i-1]
            print(*arr)
        else:
            arr[-i] = num
            print(*arr)
            break
    if num < arr[0]:
        arr[0] = num
        print(*arr)
        return
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
