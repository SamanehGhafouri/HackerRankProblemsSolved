# Given five positive integers, find the minimum
# and maximum values that can be calculated by summing
#  exactly four of the five integers. Then print the
# respective minimum and maximum values as a single
# line of two space-separated long integers.


def mini_max_sum(arr):
    sorted_arr = sorted(arr)
    sum = 0
    min_max_sum = []
    for i in range(len(sorted_arr)):
        sum += sorted_arr[i]
        max_sum = sum - sorted_arr[0]
        min_sum = sum - sorted_arr[-1]
    min_max_sum.append(min_sum)
    min_max_sum.append(max_sum)
    print(" ".join(str(x) for x in min_max_sum))


ar = [3, 2, 1, 4, 5]
print(mini_max_sum(ar))
