# Insertion sort part_2


def insertion_sort_2(n, arr):

    for i in range(1, len(arr)):
        value_to_sort = arr[i]

        while arr[i - 1] > value_to_sort and i > 0:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
        arr[i] = value_to_sort
        print(*arr)


n = int(input())
arr = list(map(int, input().rstrip().split()))
insertion_sort_2(n, arr)
print(insertion_sort_2(n, arr))