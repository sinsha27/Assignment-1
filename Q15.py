#
arr = []

def main():
  getArray()
  displayArray()

def getArray():
   n = int(input("Enter the size of array : "))
   print("Enter array elements : ")
   for i in range(n):
    v = int(input())
    arr.append(v)

def displayArray():
  print("Array =  ", arr)

main()