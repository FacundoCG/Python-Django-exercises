""" The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 

Print the average of the marks array for the student name provided, showing 2 places after the decimal. """

if __name__ == '__main__':
    n: int = int(input())
    student_marks: dict = {}

    for _ in range(n):
        name, *line = input().split() #This code will work in the following way: if you write "Hello John Doe", it assigns name = "Hello" line = ["John", "Doe"]
        scores: list = list(map(float, line))
        student_marks[name] = scores

    query_name: str = input()
    average: float = 0
    
    for i in student_marks[query_name]:
        average += i
    
    average /= 3

    format_average: float = "{:.2f}".format(average)
    
    print(format_average)
