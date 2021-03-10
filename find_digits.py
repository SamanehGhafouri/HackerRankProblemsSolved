# Find Digits
# An integer d is a divisor of an integer n if the
# remainder of n % d == 0
# Given an integer, for each digit that makes up
# the integer determine whether it is a divisor.
# Count the number of divisors occuring within the integer.


def find_digits(n):
    count = 0
    for i in str(n):

        if int(i) != 0 and n % int(i) == 0:
            count += 1
        count += 0
    return count


t = int(input())
for t_itr in range(t):
    n = int(input())
    result = find_digits(n)
    print(result)
