""" The students of District College have subscriptions to English and French newspapers. 

Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 

The same student could be in both sets. 

Your task is to find the total number of students who have subscribed to at least one newspaper. """

total_english_students: int = int(input())
english_students: set = set(map(int, input().split()))
total_french_students: int = int(input())
french_students: set = set(map(int, input().split()))

students: set = english_students.union(french_students)

print(len(students))
