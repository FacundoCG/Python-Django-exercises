""" Given a square matrix, calculate the absolute difference between the sums of its diagonals. """

import os

def diagonalDifference(arr: list)->int:
    d1: int = 0
    d2: int = 0
    n: int = len(arr)
    
    for i in range(n):
        d1 += arr[i][i]
    
    for j in range(n):
        d2 += arr[j][n-1-j]
    
    return abs(d1-d2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n: int = int(input().strip())

    arr: list = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result: int = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
