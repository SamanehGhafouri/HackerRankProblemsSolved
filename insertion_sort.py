# Insertion sort


def insertion_sort(arr):
    not_sorted_part = range(1, len(arr))
    for i in not_sorted_part:
        value_to_sort = arr[i]

        while arr[i - 1] > value_to_sort and i > 0:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1


arr = [1, 2, 4, 5, 3]
insertion_sort(arr)
for i in range(len(arr)):
    print(arr[i])
