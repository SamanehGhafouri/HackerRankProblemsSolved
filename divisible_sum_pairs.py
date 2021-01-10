# n: the integer length of array ar
# ar: an array of integers
# k: the integer to divide the pair sum by
# Find the count of pairs that follow this rule:
# i < j and ar[i] + ar[j] is divisible by k
# Example:
# input:
# 6 3
# 1 3 2 6 1 2
# out put:
# 5


def divis_sum_pairs(n, k, ar):
    count = 0
    for i in range(len(ar)):
        for j in range(len(ar)):
            if i < j:
                if (ar[i] + ar[j]) % k == 0:
                    count += 1
    return count


nk = input().split()
n = int(nk[0])
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
result = divis_sum_pairs(n, k, ar)
print(result)
