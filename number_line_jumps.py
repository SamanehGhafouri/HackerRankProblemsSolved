def kangaroo(x1, v1, x2, v2):
    if v1 > v2:
        if (x1 - x2) % (v2 - v1) == 0:
            return "YES"
    return "NO"


x1v1x2v2 = input().split()
x1 = int(x1v1x2v2[0])
v1 = int(x1v1x2v2[1])
x2 = int(x1v1x2v2[2])
v2 = int(x1v1x2v2[3])
kangaroo(x1, v1, x2, v2)