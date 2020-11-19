# Given a square matrix, calculate the
# absolute difference between the sums of its diagonals.


def diagonal_difference(arr, n):
    sum_left_diag = 0
    sum_right_diag = 0
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                sum_left_diag += arr[i][j]

            elif i == n - j - 1:
                sum_right_diag += arr[i][j]

    return abs(sum_left_diag - sum_right_diag)


ar = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
num = 3
print(diagonal_difference(ar, num))
