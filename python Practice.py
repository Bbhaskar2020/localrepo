

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-0-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr = [1, 5,3,9, 8, 70, 4, 2]
sorted_array = bubble_sort(arr)
print("These are sorted array..", sorted_array)

