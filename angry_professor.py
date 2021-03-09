# Angry Professor
# the professor decides to cancel class if fewer
# than some number of students are present when class starts.
# if arrive <= 0 ON TIME
# if arrive > 0 LATE
# k = the cancellation threshold
# a = array of arrival time


def if_class_canceled(k, a):
    count = 0
    for i in a:
        if i <= 0:
            count += 1
        else:
            count += 0
    if count >= k:
        return "NO"
    else:
        return "YES"


t = int(input())
for t_itr in range(t):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    a = list(map(int, input().rstrip().split()))
    result = if_class_canceled(k, a)
    print(result)