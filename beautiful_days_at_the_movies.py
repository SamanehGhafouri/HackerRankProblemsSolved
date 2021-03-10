# Beautiful Days at the Movies
# Given a range of numbered days,[i...j] and a number k,
# determine the number of days in the range that are beautiful.
# Beautiful numbers are defined as numbers where |i-reverse(i)| is evenly divisible by k.


def beautiful_days(i, j, k):
    count = 0
    for day in range(i, j + 1):

        if abs(day - int(str(day)[::-1])) % k == 0:
            count += 1
        count += 0
    return count


ijk = input().split()
i = int(ijk[0])
j = int(ijk[1])
k = int(ijk[2])

result = beautiful_days(i, j, k)
print("The number of Beautiful Days are: ", result)
