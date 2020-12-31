# s: integer, starting point of Sam's house location.
# t: integer, ending location of Sam's house location.
# a: integer, location of the Apple tree.
# b: integer, location of the Orange tree.
# apples: integer array, distances at which each apple falls from the tree.
# oranges: integer array, distances at which each orange falls from the tree.
# It should print the number of apples and oranges that land on Sam's house, each on a separate line.
# The first line contains two space-separated integers denoting the respective values of s and t.
# The second line contains two space-separated integers denoting the respective values a of b and.
# The third line contains two space-separated integers denoting the respective values of m and n.
# The fourth line contains m space-separated integers denoting
# the respective distances that each apple falls from point a.
# The fifth line contains n space-separated integers denoting
# the respective distances that each orange falls from point b.


def count_apples_and_oranges(s, t, a, b, apples, oranges):
    count_apples = 0
    count_oranges = 0
    added_distance_apples = []
    added_distance_oranges = []
    for i in apples:
        new_apples = i + a
        added_distance_apples.append(new_apples)
    for j in oranges:
        new_oranges = j + b
        added_distance_oranges.append(new_oranges)

    for h in added_distance_apples:
        if s <= h <= t:
            count_apples += 1
    print(count_apples)

    for o in added_distance_oranges:
        if s <= o <= t:
            count_oranges += 1
    print(count_oranges)


st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
count_apples_and_oranges(s, t, a, b, apples, oranges)
