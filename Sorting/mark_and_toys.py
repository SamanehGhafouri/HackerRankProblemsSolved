# Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants
# to buy some. There are a number of different toys lying in front of him, tagged with their prices.
# Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys
# with this money. Given a list of toy prices and an amount to spend, determine
# the maximum number of gifts he can buy.

def maximum_toys(prices, k):
    p_less_than_k = []
    for i in prices:
        if i < k:
            p_less_than_k.append(i)

    total_p = 0
    count = 0
    for p in sorted(p_less_than_k):
        if total_p > k:
            break
        elif total_p < k:
            total_p += p
            if total_p < k:
                count += 1
    return count


if __name__ == '__main__':
    arr = [1, 12, 5, 111, 200, 1000, 10, 6, 18, 9, 10]
    result = maximum_toys(arr, 50)
    print(result)
