# Two friends Anna and Brian, are deciding
# how to split the bill at a dinner. Each will
# only pay for the items they consume. Brian gets
# the check and calculates Anna's portion. You must
# determine if his calculation is correct.
# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money the Anna contributed to the bill
# n: the number of items in the bill


def bon_appetit(bill, k, b_charged):

    total_bill = sum(bill)

    for i in range(len(bill)):

        if i == k:
            b_actual = (total_bill - bill[i]) / 2

            if b_charged == b_actual:
                print('Bon Appetit')
            else:
                diff = b_charged - b_actual
                print(int(diff))


nk = input().rstrip().split()
n = int(nk[0])
k = int(nk[1])
bill = list(map(int, input().rstrip().split()))
b_charged = int(input().strip())
bon_appetit(bill, k, b_charged)