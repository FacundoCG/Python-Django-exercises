""" Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line. """

if __name__ == '__main__':
    students: list = []
    bad_students: list = []
    
    for _ in range(int(input())):
        student: list = []
        name: str = input()
        score: float = float(input())
        
        student.append(name)
        student.append(score)
        students.append(student)
    
    scores: list = list(set([i[1] for i in students]))
    scores.sort()

    for k in students:
        if k[1] == scores[1]:
            bad_students.append(k[0])
    
    bad_students.sort()
    
    for j in bad_students:
        print(j)
