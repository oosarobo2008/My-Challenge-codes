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