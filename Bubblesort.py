# def bubble(arr1):
arr1 = [7, 5, 1, 9, 2, 3, 4, 6]
n = len(arr1)
for i in range(n):
        swapped = False
    for j in range(0, n-0-1):
        if arr1[j]>arr1[j+1]:
            arr1[j], arr1[j+1]=arr1[j+1], arr1[j]
            swapped = True
    if not swapped:
        break
print("Sorted array..", arr1)



arr2 = [8, 4, 6, 9, 1, 2]
n = len(arr2)
for i in range(n):
    swapped = False
    for j in range(0, n-0-1):
        if arr2[j]>arr2[j+1]:
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]
            swapped = True
    if not swapped:
        break
print("sorted array..", arr2)
