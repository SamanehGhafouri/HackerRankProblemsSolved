def average(arr):
    avg = sum(set(arr)) / len(set(arr))
    return avg


ar = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174]
print(average(ar))
