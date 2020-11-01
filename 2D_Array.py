# Given 6 x 6 2D array. An hourglass is the a subset of values with indices falling in this pattern
# a b c
#   d
# e f g
# there are 16 hourglass in arr. An hourglass sum is the sum of an hourglass's values.
# Calculate the 16 hourglass sum and return the maximum of them


def two_d_array(arr):
    li = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            print(arr[i][j], arr[i][j + 1], arr[i][j + 2], arr[i + 1][j],
                  arr[i + 1][j + 1], arr[i + 1][j + 2], arr[i + 2][j], arr[i + 2][j + 1], arr[i + 2][j + 2])
            li.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] +
                      arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
    print(f"The max sum of hourglass in the given pattern is: {max(li)}")


input_arr = [[-9, -9, -9, 1, 1, 1], [0, -9, 0, 4, 3, 2], [-9, -9, -9, 1, 2, 3],
             [0, 0, 8, 6, 6, 0], [0, 0, 0, -2, 0, 0], [0, 0, 1, 2, 4, 0]]
print(two_d_array(input_arr))
