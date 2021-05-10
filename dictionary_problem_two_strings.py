# Given two strings, determine if they share a
# common substring. A substring may be as small as one character.


def two_strings(s1, s2):
    set_string = set()
    for ch in s1:
        set_string.add(ch)

    for ch in s2:
        if ch in set_string:
            return 'YES'
    return 'NO'


string_one = input()
string_two = input()
result = two_strings(string_one, string_two)
print(result)
