# This is a simple challenge to get things started.
# Given a sorted array (arr) and a number (V),
# can you print the index location of V in the array?


def intro(v, arr):
    for i in range(len(arr)):
        if arr[i] == v:
            print(i)


print(intro(4, [1, 4, 5, 7, 9, 12]))
