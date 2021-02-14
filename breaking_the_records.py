# Maria plays college basketball and wants to go pro.
# Each season she maintains a record of her play. She
# tabulates the number of times she breaks her season
# record for most points and least points in a game.
# Points scored in the first game establish her record
# for the season, and she begins counting from there.


def breaking_records(scores):
    count_max = 0
    count_min = 0
    min_num = scores[0]
    max_num = scores[0]
    for i in range(len(scores) - 1):
        if scores[i+1] > max_num:
            count_max += 1
            max_num = scores[i+1]
            i += 1
        elif scores[i+1] < min_num:
            count_min += 1
            min_num = scores[i+1]
            i += 1
    return count_max, count_min


n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breaking_records(scores)
print(result)
