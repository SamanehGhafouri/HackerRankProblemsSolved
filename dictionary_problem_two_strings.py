# Given two strings, determine if they share a
# common substring. A substring may be as small as one character.


def two_strings(s1, s2):
    for ch in s1:
        if ch in s2:
            return 'YES'
    return 'NO'


string_one = input()
string_two = input()
result = two_strings(string_one, string_two)
print(result)
