# A left rotation operation on an array
# shifts each of the array's elements 1 unit
# to the 2 left. For example, if  left rotations
# are performed on array [1, 2, 3, 4, 5] , then the array would become [3, 4, 5, 1, 2] .
# Given an array a  of n  integers and a number, d , perform d
# left rotations on the array. Return the updated array to
# be printed as a single line of space-separated integers.


def left_rotation(a, d):
    pop_from_front = a[d:]
    final_result = pop_from_front + a[:d]
    return final_result


arr = [1, 2, 3, 4, 5]
num_of_rotation = 4
print(left_rotation(arr, num_of_rotation))
