# find out if the string is a palindrome in 3 ways

# No function, No Loop **************************
string = "madam"
if string[:] == string[::-1]:
    print("True")
else:
    print("False")


# #Using While loop ******************************
def is_palindrome(string: str) -> bool:
    first, last = 0, len(string) - 1

    while first < last:
        if string[first] != string[last]:
            return False
        first += 1
        last -= 1
    return True


p1 = is_palindrome("madam")
print(p1)


# Using For loop *********************************
def is_palindrome(string: str) -> bool:
    for i in range(len(string) // 2):
        j = len(string) - 1 - i
        if string[i] != string[j]:
            return False
    return True


p1 = is_palindrome("madam")
print(p1)
