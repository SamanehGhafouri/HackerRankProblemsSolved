import csv
from collections import defaultdict

# Test Case
# with open("/Users/samanehghafouri/PycharmProjects/HackerRankProblems/data/array_manipulation_hard_prob_test_1", "r") as f:
#     n = 10000000
#     freader = csv.reader(f, delimiter=" ")
#     li = []
#     for line in freader:
#         li.append([int(val) for val in line])


def array_manipulation(n, li):

    li_result = defaultdict(int)

    for lo, hi, val in li:
        li_result[lo] += val
        li_result[hi + 1] += -val

    my_max = -1
    my_sum = 0
    for key in sorted(li_result.keys()):
        my_sum += li_result[key]
        my_max = max(my_max, my_sum)

    return my_max


lis = [[1, 5, 3],
      [4, 8, 7],
      [6, 9, 1]]
n = 10

max_num = array_manipulation(n, lis)
print(max_num)

