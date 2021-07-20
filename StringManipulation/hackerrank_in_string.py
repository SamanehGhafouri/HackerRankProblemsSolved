# We say that a string contains the word hackerrank if a subsequence of
# its characters spell the word hackerrank. Remember that a subsequence
# maintains the order of characters selected from a sequence.
import re


def hackerrank_inn_string(s):

    result = re.match(r"^[a-z]*h[a-z]*a[a-z]*c[a-z]*k[a-z]*e[a-z]*r[a-z]*r[a-z]*a[a-z]*n[a-z]*k[a-z]*$", s)

    if result is None:
        return "No"
    return "YES"


if __name__ == '__main__':
    string = "rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt"
    res = hackerrank_inn_string(string)
    print(res)