""" Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 

Print the decimal value of each fraction on a new line with 6 places after the decimal. """

def plusMinus(arr: list):
    positives: int = 0
    negatives: int = 0
    zero: int = 0

    for i in arr:
        if i>0:
            positives += 1
        elif i<0:
            negatives += 1
        else:
            zero += 1
    
    print(positives/len(arr))
    print(negatives/len(arr))
    print(zero/len(arr))


if __name__ == '__main__':
    n: int = int(input().strip())

    arr: list = list(map(int, input().rstrip().split()))

    plusMinus(arr)
