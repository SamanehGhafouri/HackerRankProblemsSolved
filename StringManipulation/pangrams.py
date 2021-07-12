# A pangram is a string that contains every letter of the alphabet.
# Given a sentence determine whether it is a pangram in the English
# alphabet. Ignore case. Return either pangram or not pangram as appropriate.
import string


def pangrams(s):
    alpha_lower = set(string.ascii_lowercase)
    alpha_upper = set(string.ascii_uppercase)

    if set(s.lower()) >= alpha_lower or set(s.upper()) >= alpha_upper:
        return 'pangrams'
    else:
        return 'no pangrams'


if __name__ == '__main__':
    st = 'We promptly judged antique ivory buckles for the next prize'
    st_two = 'All of the letters of the alphabet are present in the string.'
    print(pangrams('The quick brown fox jumps over the lazy dog'))
