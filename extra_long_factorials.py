# Calculate and print the factorial of a given integer


def extra_long_factorials(n):
    n_factorial = 1

    for i in range(n):
        n_factorial = (n - i) * n_factorial
    print(n_factorial)


n = int(input())
print(extra_long_factorials(n))
