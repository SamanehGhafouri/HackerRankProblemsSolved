# Reduce a string of lowercase characters in
# range ascii[‘a’..’z’]by doing a series of operations.
# In each operation, select a pair of adjacent letters that match, and delete them.
# Delete as many characters as possible using this method
# and return the resulting string. If the final string is empty, return Empty String
def super_reduced_string(s):
    stack = ["$"]
    for ch in s:
        if ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    if len(stack) == 1:
        return "Empty String"
    else:
        return "".join(stack[1:])


if __name__ == '__main__':

    st = "acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj "
    result = super_reduced_string(st)
    print(result)