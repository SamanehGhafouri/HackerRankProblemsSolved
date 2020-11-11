# Tuples
# Given an integer, n, and n space-separated
# integers as input, create a tuple t, of
# those n integers. Then compute and print the result of hash(t)

n = int(input())
rang = input().split()
t = tuple(int(i) for i in rang)
print(hash(t))
