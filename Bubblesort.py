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