""" You are given a set A and N number of other sets. These N number of sets have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements from set A. """

elements_a: int = int(input())
A: set = set(map(int, input().split()))
number_sets: int = int(input())

for i in range(number_sets):
    command: int = input()
    B: set = set(map(int, input().split()))
    
    if "intersection_update" in command:
        A.intersection_update(B)
    elif "symmetric_difference_update" in command:
        A.symmetric_difference_update(B)
    elif "difference_update" in command:
        A.difference_update(B)
    else:
        A.update(B)

suma: int = sum(A)
print(suma)