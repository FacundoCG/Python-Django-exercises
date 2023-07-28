""" You are given a set A and n other sets.

Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset. """

A: set = set(map(int, input().split()))
number_sets: int = int(input())
true_list: list = []

for i in range(number_sets):
    B: set = set(map(int, input().split()))
    
    if B.issubset(A) and A!=B:
        true_list.append(True)
    else:
        true_list.append(False)

print(all(true_list))