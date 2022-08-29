# List Comprehensions
# Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of a cuboid along with an
# integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k  is not
# equal to N. Here, 0 <= i <= X; 0 <= j <= Y; 0 <= k <= Z 

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

rank = [[a, b, c] for a in range(X + 1) for b in range(Y + 1) for c in range(Z + 1) if a + b + c != N]
print (rank)