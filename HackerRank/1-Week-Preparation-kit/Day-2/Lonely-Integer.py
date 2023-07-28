""" Given an array of integers, where all elements but one occur twice, find the unique element. """

import os

def lonelyinteger(a: list)->int:
    value: str = ''

    for i in a:
        if a.count(i)==1:
            value: int = i
    
    return value
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n: int = int(input().strip())

    a: list = list(map(int, input().rstrip().split()))

    result: int = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
