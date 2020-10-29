# Find number of repeated 'a' in the given string in a way that
# string repeated based on integer n
# Here we are looking for number of repeated 'a'


def repeated_string(s, n):
    a_in_s = s.count('a')
    count_a = a_in_s * (n // len(s)) + s[:n % len(s)].count('a')
    return count_a


lowercase_letters = 'aba'
int_n = 10
output = repeated_string(lowercase_letters, int_n)
print(output)

# --------------------------- TEST --------------------------- #
test_data = [
    ('abc', 10, 4),
    ('a', 1000000000000, 1000000000000),
    ('ab', 3, 2)
]

for item in test_data:
    expected = item[2]
    actual = repeated_string(item[0], item[1])
    print(expected == actual)