def wight_uniform_string(s, queries):
    weights = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
               'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
               'x': 24, 'y': 25, 'z': 26}

    li = list(s)
    new_li = {}
    i = 0
    while i < len(li):
        if li[i] in new_li:
            if li[i] == li[i-1]:
                new_li[li[i]] += 1
                i += 1
            else:
                new_li[li[i]] = 1
                i += 1
        else:
            new_li[li[i]] = 1
            i += 1

    new_set = set()
    for key, val in new_li.items():
        if key in weights:
            for i in range(val + 1):
                new_set.add(i * weights[key])

    q_new = []
    for q in queries:
        if q in new_set:
            q_new.append("Yes")
        else:
            q_new.append("No")
    return q_new


if __name__ == '__main__':
    st = 'aaaaaa'
    qe = [1, 9, 3, 4, 5]
    result = wight_uniform_string(st, qe)
    print(result)