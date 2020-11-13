# Set discard(), remove(), pop()
# Example Input
# 9
# 1 2 3 4 5 6 7 8 9
# 10
# pop
# remove 9
# discard 9
# discard 8
# remove 7
# pop
# discard 6
# remove 5
# pop
# discard 5
# Output
# sum of the elements in set = 4

n = int(input())
s = set(map(int, input().split()))
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))





