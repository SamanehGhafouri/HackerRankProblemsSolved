# for n = 5
# print out this in right align
#
#     #
#    ##
#   ###
#  ####
# #####


def staircase(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + '#' * i)


num = 5
print(staircase(num))
