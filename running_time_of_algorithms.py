# This is a insertion sort which will
# return the number of running time based on
# the number of shifts it will take to sort the array


def running_time(arr):

    the_running_time = 0

    for i in range(1, len(arr)):
        not_sorted_value = arr[i]

        while arr[i - 1] > not_sorted_value and i > 0:
            arr[i - 1], arr[i] = arr[i], arr[i -1]
            i -= 1
            the_running_time += 1
        arr[i] = not_sorted_value
    return the_running_time


n = int(input())
arr = list(map(int, input().rstrip().split()))
result = running_time(arr)
print(result)

