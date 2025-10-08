A = 10
print(A)
print()

S = 0.0
for i in range(A,2*A+1):
  x = i**2
  S += x
  print(i,x,S)

print(S)