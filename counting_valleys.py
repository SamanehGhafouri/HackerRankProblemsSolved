# Counting the number of time the hiker traversed valley
# "U" is going up
# "D" is going down
#
# Example: input = ['U', 'U', 'D', 'D', 'D', 'U', 'U', 'D'] output = 1
#
#  / \
# /   \    /\
# ---------------
#      \/


def counting_valleys(path):
    num = 0
    li = []
    sea_valley = []

    for i in range(len(path)):
        if path[i] == 'U':
            j = 1
            li.append(j)
        else:
            j = -1
            li.append(j)
    for k in li:
        num += k
        if num == -1:
            print("valley")
            sea_valley.append("valley")
        elif num == 0:
            print("sea level")
            sea_valley.append("sea level")

    state = "sea level"
    count = 0
    for p in sea_valley:
        if p != state:
            state = p
            print(f"change state to: {p}")
            if state == "valley":
                count += 1
    return count


p = ['U', 'D', 'D', 'U', 'U', 'D', 'D', 'U', 'U', 'D', 'D', 'D', 'U', 'D', 'U', 'U']
s = 8
fin = counting_valleys(p)
print(fin)

# --------------------------- TEST ----------------------------------- #
test_data = [
    (['U', 'D', 'D', 'D', 'U', 'D', 'U', 'U'], 1),
    (['D', 'U'], 1),
    (['U', 'U', 'D', 'U', 'D', 'D', 'D', 'U', 'D', 'D', 'U', 'U', 'U', 'D'], 2)

]

for item in test_data:
    expected = item[1]
    actual = counting_valleys(item[0])
    print(expected == actual, expected, actual)
