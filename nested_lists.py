# Create an nested list of names and scores
# Find the second minimum score
# If more than one person has the second minimum score
# Print the names of those people in alphabetical sorted order

# Original code
if __name__ == '__main__':
    list_names_scores = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        list_names_scores.append([name, score])
        list_names_scores.sort(key=lambda x: x[1])

    first_min = list_names_scores[0]
    second_min = None

    for t in list_names_scores:
        if t[1] > first_min[1]:
            second_min = t
            break

    names = []
    for i in list_names_scores:
        if i[1] == second_min[1]:
            names.append(i[0])

    for j in sorted(names):
        print(j)

# ----------------------------------- My Example ----------------------------------------
# arr = [['x', 30], ['d', 10], ['g', 20], ['t', 50], ['a', 20], ['o', 10]]
# arr.sort(key=lambda x: x[1])
#
#
# first_min = arr[0]
# second_min = None
# for t in arr:
#     if t[1] > first_min[1]:
#         second_min = t
#         break
#
#
# names = []
# for i in arr:
#     if i[1] == second_min[1]:
#         names.append(i[0])
#
#
# for j in sorted(names):
#     print(j)