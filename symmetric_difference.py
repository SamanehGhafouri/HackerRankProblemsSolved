# Symmetric Difference between M and N
# Print elements that are in M and N but not in Both

len_m = int(input())
input_m = input().split()
set_m = set(map(int, input_m))
len_n = int(input())
input_n = input().split()
set_n = set(map(int, input_n))


symmetric_difference = sorted(set_m.union(set_n) - set_m.intersection(set_n))
for i in symmetric_difference:
    print(i)
