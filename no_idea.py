# we have a list of integers n, and m number as 2  disjoint sets a and b
# if the number in set a and also in n, we add 1 for each similar number
# if the number in set b and also in n , we substract 1

len_n, len_m = input().split()

n = list(input().split())
a = set(input().split())
b = set(input().split())
print(sum((i in a) - (i in b) for i in n))


# ---------------------- Not Efficient Way ----------------------- #
len_n, len_m = input().split()
count_happiness = 0
n = list(input().split())
a = set(input().split())
b = set(input().split())

for i in a:
    if i in n:
        count_happiness += 1

for i in b:
    if i in n:
        count_happiness -= 1

print(count_happiness)
