""" You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False. """

number_test_cases: int = int(input())

for i in range(number_test_cases):
    number_elements_A: int = int(input())
    A: set = set(map(int, input().split()))
    
    number_elements_B: int = int(input())
    B: set = set(map(int, input().split()))
    
    print(A.issubset(B))
