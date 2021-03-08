# New Year Chaos
# It is New Year's Day and people are in line for the Wonderland rollercoaster
# ride. Each person wears a sticker indicating their initial position in the queue from 1 to n.
# Any person can bribe the person directly in front of them to swap positions,
# but they still wear their original sticker. One person can bribe at most two others.
# Determine the minimum number of bribes that took place to get to a
# given queue order. Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.


def minimum_bribes(q):
    moves = 0

    for i in range(len(q)-1, -1, -1):
        difference = q[i] - (i + 1)
        if abs(difference) > 2:
            print("Too chaotic")
            return
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                moves += 1
    print(moves)


t = int(input())
for num in range(t):
    n = int(input())

    q = list(map(int, input().rstrip().split()))

    minimum_bribes(q)
