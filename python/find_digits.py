from math import log10


def find_digits_in_int(num):
    log_num = int(log10(num)) + 1
    return log_num


if __name__ == '__main__':
    n = 1234
    result = find_digits_in_int(n)
    print(result)
