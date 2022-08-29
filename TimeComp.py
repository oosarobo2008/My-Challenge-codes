# Problem: You are given an integer n. Count the total of 1 + 2 + . . . + n.

def model(n):
  result = n*(n+1)//2
  return result

n = int(input('Enter Value:'))
(result) = model(n)
print(result)