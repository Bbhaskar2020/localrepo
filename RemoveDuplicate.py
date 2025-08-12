list = [2, 4, 5, 4, 5, 8]
def rem_duplicate(list):
    result= []
    seen = set()
    for item in list:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result
print(rem_duplicate(list))