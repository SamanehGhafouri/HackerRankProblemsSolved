# Migratory Birds
# Given an array of bird sightings where every element
# represents a bird type id, determine the id of the most
# frequently sighted type. If more than 1 type has been spotted
# that maximum amount, return the smallest of their ids.


def migratory_bird(arr):
    dic = {}
    for i in range(len(arr)):
        if arr[i] in dic:
            dic[arr[i]] += 1
        else:
            dic[arr[i]] = 1

    li_keys = []
    max_value = max(dic.values())
    for key, value in dic.items():
        if value == max_value:
            li_keys.append(key)
    return min(li_keys)


arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = migratory_bird(arr)
print(result)
