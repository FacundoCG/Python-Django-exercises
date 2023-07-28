""" The students of District College have subscriptions to English and French newspapers. 

Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 

The same student could be in both sets. 

Your task is to find the total number of students who have subscribed to either the English or the French newspaper but not both. """

total_english_students: int = int(input())
english_students: set = set(map(int, input().split()))
total_french_students: int = int(input())
french_students: set = set(map(int, input().split()))

students_in_one_class: set = english_students.symmetric_difference(french_students)

print(len(students_in_one_class))