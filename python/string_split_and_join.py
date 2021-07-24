# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.
def string_split_join(line):
    to_list = line.split(" ")
    join_list = "-".join(to_list)
    return join_list


if __name__ == '__main__':
    st = "this is a string"

    result = string_split_join(st)
    print(result)
