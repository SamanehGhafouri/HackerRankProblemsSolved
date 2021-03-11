# Append and Delete
# You have two strings of lowercase English letters. You can perform two types of operations on the first string:
# 1. Append a lowercase English letter to the end of the string.
# 2. Delete the last character of the string. Performing this operation on an empty string results in an empty string.
# Given an integer,k , and two strings,s and t, determine whether
# or not you can convert s to t by performing exactly k of the above
# operations on s. If it's possible, print Yes. Otherwise, print No.


def append_delete(s, t, k):
    smallest = s if len(s) < len(t) else t

    len_match_ch = 0
    for i in range(len(smallest)):
        if s[i] == t[i]:
            len_match_ch += 1
        else:
            break
    not_match_in_t = len(t) - len_match_ch
    not_match_in_s = len(s) - len_match_ch
    total_not_match = not_match_in_t + not_match_in_s

    total_len_t_and_s = len(s) + len(t)

    if len(t) > len(s):
        return "No"

    else:

        if k < total_len_t_and_s:
            if len_match_ch == 0:
                return "No"
            else:
                if k >= total_not_match:
                    return "Yes"
                return "No"
        elif len(t) > len(s):

            return "No"

        return "Yes"


s = input()
t = input()
k = int(input())
result = append_delete(s, t, k)
print(result)
