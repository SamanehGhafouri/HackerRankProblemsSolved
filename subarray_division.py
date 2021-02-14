# Given a chocolate bar, two children, Lily and Ron, are determining
# how to share it. Each of the squares has an integer on it.
# Lily decides to share a contiguous segment of the bar selected such that:
# The length of the segment matches Ron's birth month, and,
# The sum of the integers on the squares is equal to his birth day.
# s: an array of integers, the numbers on each of the squares of chocolate
# d: an integer, Ron's birth day
# m: an integer, Ron's birth month


def birthday(s, d, m):
    count = 0

    for i in range(len(s) + 1 -  m):
        if sum(s[i:i+m]) == d:
            count += 1
    return count


n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
result = birthday(s, d, m)
print(result)