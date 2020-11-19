# Given an array of integers, calculate the ratios of its elements that are positive,
#  negative, and zero. Print the decimal value of each fraction on
#  a new line with 6 places after the decimal.


def plus_minus(arr):
    count_negative_nums = 0
    count_positive_nums = 0
    count_zeros = 0
    li = []
    for i in arr:
        if i < 0:
            count_negative_nums += 1
            negatives = count_negative_nums / len(arr)

        elif i > 0:
            count_positive_nums += 1
            positives = count_positive_nums / len(arr)

        else:
            count_zeros += 1
            zeroes = count_zeros / len(arr)

    li.append(positives)
    li.append(negatives)
    li.append(zeroes)
    for i in li:
        print("{0:.6f}".format(i))


ar = [-4, 3, -9, 0, 4, 1]
print(plus_minus(ar))
