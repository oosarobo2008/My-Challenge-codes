def Reserve(A):
  A.reverse()
  return A

def Append(B):
  B.append('Yes')
  B.sort()
  return B

(A) = ['Tom','Joy','Ink','Neck','Hen']
(B) = Reserve(A)
(C) = Append(B)
print(C)