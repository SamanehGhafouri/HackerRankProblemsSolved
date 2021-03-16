# Insertion sort part-1


def insertion_sort_1(n, arr):
    i = n - 1
    target = arr[i]
    while i > 0 and target < arr[i - 1]:
        arr[i] = arr[i-1]
        print(*arr)
        i -= 1
    arr[i] = target
    print(*arr)


arr = [2, 4, 6, 8, 3]
print(insertion_sort_1(5,arr))