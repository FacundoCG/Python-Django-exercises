""" Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 

You are given n scores. Store them in a list and find the score of the runner-up. """

if __name__ == '__main__':
    n: int = int(input())
    arr: list = list(map(int, input().split()))
        
    arr.sort(reverse=True)
    
    runner_up_score: int = 0
    
    for i in range(n):
            
        if arr[i] != max(arr):
            runner_up_score = arr[i]
            break
    
    print(runner_up_score)
