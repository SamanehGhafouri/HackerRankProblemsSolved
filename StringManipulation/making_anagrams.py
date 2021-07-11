from collections import Counter
# A student is taking a cryptography class and has found anagrams to be very useful.
# Two strings are anagrams of each other if the first string's letters can be rearranged to
# form the second string. In other words, both strings must contain the same exact letters in
# the same exact frequency. For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
# The student decides on an encryption scheme that involves two large strings. The encryption is
# dependent on the minimum number of character deletions required to make the two strings anagrams.
# Determine this number.
# Given two strings, a and b, that may or may not be of the same length, determine
# the minimum number of character deletions required to make a and b anagrams.
# Any characters can be deleted from either of the strings.


def make_anagram(a, b):
    ac = Counter(a)
    bc = Counter(b)

    total = 0
    for char, count in ac.items():
        if char in bc:
            total += 2*min(count, bc[char])
    return len(a) + len(b) - total


if __name__ == '__main__':
    first = 'fcrxzwscanmligyxyvym'
    second = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'
    result = make_anagram(first, second)
    print(result)