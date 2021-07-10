# Given an array of integers, sort the array in ascending order using
# the Bubble Sort algorithm above. Once sorted, print the following three lines:
# 1. Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place.
# 2. First Element: firstElement, where firstElement is the first element in the sorted array.
# 3. Last Element: lastElement, where lastElement is the last element in the sorted array.
# Hint: To complete this challenge, you must add a variable that
# keeps a running tally of all swaps that occur during execution.

def countSwaps(a):
    sorted_a = False
    count_swaps = 0
    while not sorted_a:
        sorted_a = True
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                sorted_a = False
                a[i], a[i + 1] = a[i + 1], a[i]
                count_swaps += 1
    print(f"Array is sorted in {count_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")


if __name__ == '__main__':
    arr = [9, 2, 4, 1, 6, 33, 11, 88, 0, 5]
    print(countSwaps(arr))