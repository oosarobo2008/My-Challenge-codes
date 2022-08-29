# The provided code stub will read in a dictionary containing key/value pairs of name:[marks]
# for a list of students. Print the average of the marks array for the student name provided, 
# showing 2 places after the decimal.
# The first line contains the integer , the number of students' records. 
# The next  lines contain the names and marks obtained by a student, each value separated by a space. 
# The final line contains query_name, the name of a student to query.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        line = input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = input()
    marks = 0
    for i in student_marks[query_name]:
        marks = marks + i
    avg = marks/3
    print("%.2f" %avg)