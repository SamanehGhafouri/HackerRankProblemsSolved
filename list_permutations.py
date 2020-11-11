# List Comprehension
# If 0 <= i <= x
# If 0 <= j <= y
# If 0 <= k <= z
# If i + j + k is not n

print("x = ")
x = int(input())

print("y = ")
y = int(input())

print("z = ")
z = int(input())

print("n = ")
n = int(input())

listijk = []
for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                listijk.append([i, j, k])

print(listijk)

