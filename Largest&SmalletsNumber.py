list = [20, 100, 2, 50]
count = len(list)
for i in range(count):
    swapped = False
    for j in range(0, count-0-1):
        if list[j]>list[j+1]:
            list[j], list[j+1]= list[j+1], list[j]
            swapped = True
    if not swapped:
        break
print("Number swapped..", list)
