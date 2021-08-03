from collections import Counter


def wight_uniform_string(s, queries):
    weights = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
               'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
               'x': 24, 'y': 25, 'z': 26}

    st = Counter(s)
    u_set = set()
    for ch, count in st.items():
        for i in range(1, count + 1):
            # print(i*weights[ch])
            # st[ch] = count * weights[ch]
            u_set.add(i*weights[ch])

    li_Y_N = []
    for i in queries:
        if i in u_set:
            li_Y_N.append("Yes")
        else:
            li_Y_N.append("No")
    return li_Y_N


if __name__ == '__main__':
    st = 'abbcccdddd'
    qe = [1, 7, 5, 4, 15]
    result = wight_uniform_string(st, qe)
    print(result)