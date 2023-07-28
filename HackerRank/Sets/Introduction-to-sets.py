""" Ms. Gabriel Williams is a botany professor at District College. 

One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used: sum of distintic heights/total number of distinct heights """

def average(array:list)->float:
    conjunto: set = set(array)
    promedio: float = round(sum(conjunto)/len(conjunto),3)
        
    return promedio
    
if __name__ == '__main__':
    n: int = int(input())
    arr: list = list(map(int, input().split()))
    result: float = average(arr)
    print(result)