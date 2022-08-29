# Given the names and grades for each student in a class of N students, 
# store them in a nested list and print the name(s) of any student(s)
#  having the second lowest grade.
# Note: If there are multiple students with the second lowest grade,
#  order their names alphabetically and print each name on a new line.
from tkinter import X
marks = []
gradelist = []
if __name__ == '__main__':
    for _ in range(int(input('Enter number of records:'))):
        name = input('Enter Student Name: ')
        score = float(input('Enter Score:'))
        marks += [[name,score]]
        gradelist += [score]
    x=sorted(list(set(gradelist)))[1] 
    for a,c in sorted(marks):
        if c == x:
            print(a)