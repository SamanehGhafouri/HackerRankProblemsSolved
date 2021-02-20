# A teacher asks the class to open their
# books to a page number. A student can
# either start turning pages from the front
# of the book or from the back of the book.
# They always turn pages one at a time. When
# they open the book, page 1 is always on the right side:


def page_count(n, p):
    print(min(p//2, n//2 - p//2))


n = int(input())
p = int(input())
page_count(n, p)
