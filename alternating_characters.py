# Alternating Characters
# You are given a string containing characters A and B only.
# Your task is to change it into a string such that there are
# no matching adjacent characters. To do this, you are allowed
# to delete zero or more characters in the string.
# Your task is to find the minimum number of required deletions.


def alternating_characters(s):
    num_of_removes = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            num_of_removes += 1
    return num_of_removes


q = int(input())
for q_itr in range(q):
    s = input()
    result = alternating_characters(s)
    print(result)