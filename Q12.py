#
r = int(input("Enter no. of rows : "))
c = int(input("Enter no. of columns : "))

print("\nEnter elements of Array 1 : ")
arr1 = []
for i in range(r):
  n = []
  for j in range(c):
    val = int(input())
    n.append(val)
  arr1.append(n)

print("\nEnter elements of Array 2 : ")
arr2 = []
for i in range(r):
  n = []
  for j in range(c):
    val = int(input())
    n.append(val)
  arr2.append(n)

print("\n2D Array 1 : ")
for i in arr1:
  print(i)

print("\n2D Array 2 : ")
for i in arr2:
  print(i)

s = []
for i in range(r):
  n = []
  for j in range(c):
    n.append(arr1[i][j] + arr2[i][j])
  s.append(n)

print("\nSum of Matrices:")
for i in s:
    print(i)