
# Find the Runner-Up Score! in Python 
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.
# The first line contains n. The second line contains an array A[] of n integers each separated by a space.
if __name__ == '__main__':
    n = int(input('Enter number of scores: '))
    arr = map(int, input('Put in the array:').split())
    print(sorted(list(set(arr)))[-2])
    