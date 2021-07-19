# Louise joined a social networking site to stay in touch with her friends. The signup page required her
# to input a name and a password. However, the password must be strong. The website considers a password
# to be strong if it satisfies the following criteria:
# Its length is at least 6
# It contains at least one digit
# It contains at least one lowercase English character
# It contains at least one uppercase English character
# It contains at least one special character. the special characters are: !@#$%^&*()-+
# find the minimum number of characters she must add to make her password strong


def minimum_number(password):
    numbers = set("0123456789")
    lower_case = set("abcdefghijklmnopqrstuvwxyz")
    upper_case = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    special_characters = set("!@#$%^&*()-+")

    len_numbers = len(numbers)
    len_lowercase = len(lower_case)
    len_uppercase = len(upper_case)
    len_special_ch = len(special_characters)

    for ch in password:
        if ch in numbers:
            numbers.remove(ch)
        if ch in lower_case:
            lower_case.remove(ch)
        if ch in upper_case:
            upper_case.remove(ch)
        if ch in special_characters:
            special_characters.remove(ch)

    count = 0
    len_pass = 6 - len(password)
    if len(password) >= 6:
        if len(numbers) == len_numbers:
            count += 1
        if len(lower_case) == len_lowercase:
            count += 1
        if len(upper_case) == len_uppercase:
            count += 1
        if len(special_characters) == len_special_ch:
            count += 1
    else:

        if len(numbers) == len_numbers:
            count += 1
        if len(lower_case) == len_lowercase:
            count += 1
        if len(upper_case) == len_uppercase:
            count += 1
        if len(special_characters) == len_special_ch:
            count += 1

    return max((count, len_pass))


if __name__ == '__main__':
    p = "Ab1"
    result = minimum_number(p)
    print(result)