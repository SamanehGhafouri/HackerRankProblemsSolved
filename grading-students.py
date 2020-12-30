# Grading Students
# If the diff betw the grade and the next multiple of 5 is less than 3,
# round grade up to the next multiple of 5.
# If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
# 0 <= grades[i] <= 100


def grading_students(grades):
    new_li = []
    for grade in grades:
        if grade not in range(37, 100):
            new_li.append(grade)
        else:
            new = round(grade / 5)
            new_grade = new * 5
            if new_grade > grade:
                new_li.append(new_grade)
            else:
                new_li.append(grade)
    return new_li





grades = []
grades_count = int(input())
for _ in range(grades_count):
    grades_item = int(input())
    grades.append(grades_item)

s = grading_students(grades)
print(s)






















