def fast_solution(A, B, m):
  n = len(A)
  sum_a = sum(A)
  sum_b = sum(B)
  d = sum_b - sum_a
  if d % 2 == 1:
    return False
  d //= 2
  count = count(A, m)
  for i in range(n):
    if 0 <= B[i] - d and B[i] - d <= m and count[B[i] - d] > 0:
      return True
  return False

m = 3
A =[3,9]
B = [9,0]
(G) = fast_solution(A, B, m)
print(G)

