# You are given a number of sticks of varying
# lengths. You will iteratively cut the sticks
# into smaller sticks, discarding the shortest pieces
# until there are none left. At each iteration you will
# determine the length of the shortest stick remaining,
# cut that length from each of the longer sticks and then
# discard all the pieces of that shortest length. When all
# the remaining sticks are the same length, they cannot be
# shortened so discard them.
# Given the lengths of n sticks, print the number of sticks that
# are left before each iteration until there are none left.


def cut_the_sticks(arr):
    li = []
    while len(arr) >= 1:
        li.append(len(arr))
        minimum = min(arr)
        arr = [i - minimum for i in arr if i != minimum]
    return li


ar = [5, 4, 4, 2, 2, 8]
li = cut_the_sticks(ar)
print(li)
