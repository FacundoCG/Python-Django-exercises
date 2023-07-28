""" Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.

Then print the respective minimum and maximum values as a single line of two space-separated long integers. """

import math
import os
import random
import re
import sys

def miniMaxSum(arr: list):
    sum: int = 0
    sums: list = []
    
    for i in arr:
        sum += i

    sums: list = [sum]*5
    
    for n in range(5):
        sums[n] -= arr[n]
    
    print(min(sums), max(sums))
        
if __name__ == '__main__':

    arr: list = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
