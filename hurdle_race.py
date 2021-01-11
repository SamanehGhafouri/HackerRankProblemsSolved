# A video player plays a game in which the character competes
# in a hurdle race. Hurdles are of varying heights, and the
# characters have a maximum height they can jump. There is a
# magic potion they can take that will increase their maximum
# jump height by 1 unit for each dose. How many doses of the potion
# must the character take to be able to jump all of the hurdles. If
# the character can already clear all of the hurdles, return 0.
# height = array of heights
# n, k,  the number of hurdles and the maximum height the character can jump naturally

def hurdle_race(k, height):
    maxi = max(height)
    if k >= maxi:
        return 0
    if k < maxi:
        diff = abs(maxi - k)
    return diff


nk = input().split()
n = int(nk[0])
k = int(nk[1])
height = list(map(int, input().rstrip().split()))
result = hurdle_race(k, height)
print(result)