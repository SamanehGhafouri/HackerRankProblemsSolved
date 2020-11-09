# Capitalize each first ch in words
def solve(s):
    for i in s.split():
        s = s.replace(i, i.capitalize())
    return s


full_name = 'samaneh ghafouri'
print(solve(full_name))
