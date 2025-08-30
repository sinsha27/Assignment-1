#
n = 10
for i in range(4, 0, -1):
  for j in range(n-i+1, n+1):
    print(j, end=" ")
  print("\n")
  n = n-i