#
n = int(input("Enter size of Array 1: "))
arr1 = []
print("Enter elements of Array 1: ")
for i in range(n):
    v = int(input())
    arr1.append(v)
print("Array 1:",arr1)

arr2 = arr1.copy()
e = int(input("Enter an extra element to add in Array 2: "))
arr2.append(e)

print("\nBefore Swapping")
print("Array 1:", arr1)
print("Array 2:", arr2)

arr1, arr2 = arr2, arr1

print("\nAfter Swapping")
print("Array 1:", arr1)
print("Array 2:", arr2)
