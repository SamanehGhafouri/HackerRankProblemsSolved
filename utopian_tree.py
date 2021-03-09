# Utopian Tree
# The Utopian Tree goes through 2 cycles of growth every year.
# Each spring, it doubles in height. Each summer, its height increases by 1 meter.


def utopia_tree(n):
    growth = 1
    for i in range(1, n+1):
        if i % 2 != 0:
            growth *= 2
        else:
            growth += 1
    return growth


t = int(input())
for t_itr in range(t):
    n = int(input())

    result = utopia_tree(n)
    print(result)

