#  jumpingOnClouds function should return the minimum number of jumps required, as an integer.
# c: an array of binary integers
# we can jump in a cloud including 0, only. The cloud including 1 is forbidden to go to.
# we are allowed to jump only 1 or 2 cloud at a time.
# we always can win


def min_num_of_jumps(c):
    count = 0
    i = 0
    while i < len(c):
        count += 1
        j = i + 2
        if j >= len(c) or c[j] == 1:
            i += 1
        else:
            i = j
    return count - 1


arr = [0, 0, 1, 0, 0, 1, 0]
print(min_num_of_jumps(arr))

# ---------------------- TEST ----------------------- #
test_data = [
    ([0, 0, 1, 0, 0, 1, 0], 4),
    ([0, 0, 0, 0, 1, 0], 3),
    ([0, 0, 0, 1, 0, 0], 3)
]
for item in test_data:
    expected = item[1]
    actual = min_num_of_jumps(item[0])
    print(expected == actual)