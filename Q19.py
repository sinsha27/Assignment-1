#

class addition:

  arr1 = []
  arr2 = []

  def getArray(self, n):
    print("Enter elements of Array 1 : ")
    for i in range(n):
      e = []
      for j in range(n):
        v = int(input())
        e.append(v)
      self.arr1.append(e)

    print("Enter elements of Array 2 : ")
    for i in range(n):
      e = []
      for j in range(n):
        v = int(input())
        e.append(v)
      self.arr2.append(e)

  def addArray(self, n):
    s = []
    for i in range(n):
      e = []
      for j in range(n):
        e.append(self.arr1[i][j] + self.arr2[i][j])
      s.append(e)

    print("\nSum of Matrices:")
    for i in s:
      print(i)

  def displayArray(self):
    print("\n2D Array 1 : ")
    for i in self.arr1:
      print(i)

    print("\n2D Array 2 : ")
    for i in self.arr2:
      print(i)

def main():
  a = addition()
  size = int(input("Enter size of array : "))
  a.getArray(size)
  a.displayArray()
  a.addArray(size)

main()
 