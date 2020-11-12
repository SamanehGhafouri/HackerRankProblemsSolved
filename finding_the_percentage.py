# Finding the percentage
# The provided code stub will read in a dictionary containing key/value
# pairs of name:[marks] for a list of students. Print the average of the
# marks array for the student name provided, showing 2 places after the decimal.

n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

for key, value in student_marks.items():
    print(key, value)
    if key == query_name:
        sum_of_value = sum(value) / len(value)
print('%.2f' % sum_of_value)

