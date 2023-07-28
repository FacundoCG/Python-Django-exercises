""" Given a list of integers, count and return the number of times each value appears as an array of integers. """

import os

def countingSort(arr: list)->list:
    list:list = []
    
    for i in range(len(arr)):
        if i<100:
            n = arr.count(i)
            list.append(n)
        
    return list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n: int = int(input().strip())

    arr: list = list(map(int, input().rstrip().split()))

    result: list = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
