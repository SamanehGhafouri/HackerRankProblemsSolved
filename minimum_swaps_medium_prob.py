# You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n]
# without any duplicates. You are allowed to swap any two elements.
# Find the minimum number of swaps required to sort the array in ascending order.


def minimum_swaps_to_sort(li):

    i = 1
    swaps = 0
    while i <= len(li):

        val = li[i - 1]
        if i == val:
            i += 1
        else:
            li[i - 1] = li[val - 1]
            li[val - 1] = val
            swaps += 1
    return swaps
