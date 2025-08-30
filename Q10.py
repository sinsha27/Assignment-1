#
n = int(input("Enter size : "))
arr = []
print("Enter elements of array : ")
for i in range(n):
  v = int(input())
  arr.append(v)
print("Array before sorting : ",arr)

#Selection sort
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if arr[j] < arr[min_index]:
       min_index = j
  arr[i], arr[min_index] = arr[min_index], arr[i]

print("Sorted array using selection sort : ",arr)

#Insertion sort
for i in range(1, n):
    key = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = key

print("Sorted array using insertion sort :", arr)

#Bubble sort
for i in range(n-1):
    for j in range(n-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array using bubble sort :", arr)
