# Designer PDF Viewer


def designer_pdf_viewer(h, word):
    return len(word) * max([h[ord(i) - 97] for i in word])


h = list(map(int, input().rstrip().split()))
word = input()
result = designer_pdf_viewer(h, word)
print(result)